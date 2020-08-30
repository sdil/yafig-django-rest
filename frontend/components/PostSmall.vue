<template>
  <div class="tile is-4">
      <nuxt-link :to="'/p/' + id">
            <img :src="image" :alt="'photos by' + userId" width="550"/>
      </nuxt-link>
  </div>
</template>

<script>
export default {
    name: "PostSmall",
    props: ["id", "image", "user"]
}
</script>

<style scoped>

.tile {
  justify-content: center;
}

.tile img {
  max-height: 400px;
  width: auto;
  overflow: hidden;
  left: 50%;
}

</style>