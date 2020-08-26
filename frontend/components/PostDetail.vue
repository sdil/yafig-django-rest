<template>
  <div>
    <img :src="img"/>
    <br>
    1 like
    <br>
    Sweet canyon
    posted by <nuxt-link :to="'/u/' + userid">  {{ userid }} </nuxt-link>
    <br> <strong>Comments:</strong>
    <br>
    Heidi: Nice view
  </div>
</template>

<script>
export default {
    name: "PostDetail",
    props: ["id", "userid", "img"]
}
</script>

<style>

</style>