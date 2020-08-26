<template>
  <section class="section">
      <div class="container">
        <h1 class="title">WTH is this anyway?</h1>
        <h2 class="subtitle">
          TLDR: I'm building a real product as part of my learning process. <br>
          Checkout the
          <b-tooltip label="github.com/yafig" position="is-bottom">
                 <a href="https://github.com/yafig/">official Github repositories</a>
          </b-tooltip>
        </h2>
        <p>
            Learning is fun. It's more fun when you have something to show to people.
            I've been learning a lot of things lately, and now I want to put them into a real product/project.
        </p>
        <p>
            I can never feel the whole process until I get my hand dirty. I will documents most of the 
            process of building this project in my Medium posts.
        </p>

        <p>
          Also, huge thanks to these guys for their awesome tutorials:
        </p>
        <ul>
          <li>Traversy Media - <a href="https://www.youtube.com/watch?v=ltzlhAxJr74">NuxtJS Crash Course</a></li>
          <li>DigitalOcean - <a href="https://www.digitalocean.com/community/tutorials/implementing-authentication-in-nuxtjs-app">Implementing Authentication in NuxtJS app</a></li>
        </ul>

      </div>
  </section>
</template>

<script>
export default {

}
</script>

<style>
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
  display: block;
  margin-top: 1vh;
  font-weight: bolder;
  font-size: 50px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 20px;
  color: #526488;
  padding-bottom: 15px;
}

</style>