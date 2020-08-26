module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'YAFIG - Yet Another Free (OSS) Instagram-clone',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'YAFIG Frontend in NuxtJS' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  modules: [
	  '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/sentry',
    'nuxt-buefy',
    "@nuxtjs/google-analytics"
  ],
  sentry: {
    dsn: process.env.SENTRY_DSN || 'http://dsn.com',
    config: {}, // Additional config
  },
  axios: {
	  baseURL: process.env.BASE_URL || 'http://localhost:8000'
  },
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: {url: 'users/login', method: 'post', propertyName: 'access'},
          user: {url: 'users/', method: 'get', propertyName: 'username'},
          logout: false
        },
        // We'll be using cookies once NuxtJS & Django SimpleJWT fully supports them
        tokenRequired: true
      },
      localRefresh: {
        scheme: 'refresh',
        refresh: {
          url: 'users/refresh'
        },
        token: {
          property: 'access',
          maxAge: 15
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
          maxAge: false
        }
      },
    }
  },
  googleAnalytics: {
    id: "UA-159838013-1"
  },
  plugins: [
    {src: "~plugins/ga.js", mode: "client"}
  ]
}

