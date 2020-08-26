<template>
  <div class="big-post">
            <b-icon icon="account" size="is-medium"/>
            <nuxt-link :to="'/u/' + userid">  {{ userid }}</nuxt-link><br>
    Posted 3 hours ago
    <img :src="img"/>
    <br>
    Post id {{ id }}
    <b-taglist>
        <b-tag rounded type="is-white">Nature</b-tag>
        <b-tag rounded type="is-white">Bird</b-tag>
    </b-taglist>
  </div>
</template>

<script>
export default {
    name: "PostBig",
    props: ["id", "userid", "img", "name"]
}
</script>

<style scoped>
.big-post {
  padding: 1rem;
  border: 1px dotted #ccc;
  margin: 1rem 0;
}
</style>