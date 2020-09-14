<template>
  <section class="section">
    <div class="container">
      <div v-if="post == null && error == null">Loadingg..</div>
      <div class="content" v-else-if="error != null">
        <h1>Opsss...</h1>
        {{ error.message }}
      </div>
      <div v-else>
        <PostBig :id="post.id" :image="post.image" :user="post.created_by" />
      </div>
    </div>
  </section>
</template>

<script>
import PostBig from "~/components/PostBig";

export default {
  components: {
    PostBig,
  },
  data() {
    return {
      id: "",
      post: null,
      error: null,
    };
  },
  async fetch() {
    this.id = this.$route.params.id;
    this.post = await this.$axios
      .$get("/posts/" + this.id + "/")
      .catch((error) => {
        this.error = error;
      });
  },
};
</script>