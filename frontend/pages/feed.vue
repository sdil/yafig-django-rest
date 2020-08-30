<template>
  <section class="section">
    <div class="container">
      <div id="feed">
        <PostBig
          v-for="item in posts"
          :key="item.id"
          :id="item.id"
          :userid="item.posted_by"
          :img="item.image"
          :caption="item.caption"
        />
      </div>
    </div>
  </section>
</template>

<script>
import PostBig from "~/components/PostBig";
import axios from "axios";

export default {
  middleware: "auth",
  components: {
    PostBig,
  },
  created() {
    this.$axios
      .$get("posts/")
      .then((response) => {
        this.posts = response;
        console.log(this.posts);
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
  data() {
    return {
      posts: "",
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