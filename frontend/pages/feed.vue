<template>
  <section class="section">
    <div class="container">
      <div class="content" v-if="error != null">
        <h1>Opsss...</h1>
        {{ error.message }}
      </div>
      <div v-else id="feed">
        <PostBig
          v-for="item in posts"
          :key="item.post.id"
          :id="item.post.id"
          :user="item.post.posted_by"
          :image="item.post.image"
          :caption="item.post.caption"
        />
      </div>
    </div>
  </section>
</template>

<script>
import PostBig from "~/components/PostBig";

export default {
  middleware: "auth",
  components: {
    PostBig,
  },
  created() {
    this.$axios
      .$get("posts/timeline/")
      .then((response) => {
        this.posts = response;
        console.log(this.posts);
      })
      .catch((error) => {
        this.error = error
      });
  },
  data() {
    return {
      posts: "",
      error: null,
    };
  },
};
</script>

<style scoped>
#feed {
  justify-content: center;
  align-items: center;
  width: 60%;
}
</style>