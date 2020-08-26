<template>
<section class="container">
  <h1 class="title">
    YAFIG
  </h1>
  <h2 class="subtitle">
    Yet Another Free (OSS) Instagram-clone
  </h2>
   <b-carousel :indicator-inside="false">
        <b-carousel-item v-for="(item, i) in 6" :key="i">
            <span class="image">
              <img :src="getImgUrl(i)">
            </span>
        </b-carousel-item>
    </b-carousel>
</section>
</template>

<script>
import AppLogo from '~/components/AppLogo.vue'

export default {
  components: {
    AppLogo
  },
  beforeMount(){
    this.redirectLoggedInUser()
  },
  data() {
        return {
            carousel: 0,
            animated: 'fade',
            drag: false,
            autoPlay: true,
            pauseHover: false,
            pauseInfo: false,
            repeat: false,
            pauseType: 'is-primary',
            interval: 3000,
            carousels: [
                { title: 'Slide 1', color: 'dark' },
                { title: 'Slide 2', color: 'primary' },
                { title: 'Slide 3', color: 'info' },
                { title: 'Slide 4', color: 'success' },
                { title: 'Slide 5', color: 'warning' },
                { title: 'Slide 6', color: 'danger' }
            ]
        }
    },
    methods: {
      getImgUrl(value) {
            value += 50
            return `https://picsum.photos/id/10${value}/1230/500`
        },
      redirectLoggedInUser(){
        if (this.$auth.user) {
          this.$router.push('/feed')
        }
      }
    }
}
</script>

<style scoped>
/* .carousel {
  min-height: 50vh;
}

.carousel-items {
  min-height: 50vh;
} */

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  margin-top: 1vh;
  font-weight: bolder;
  font-size: 80px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 22px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>

