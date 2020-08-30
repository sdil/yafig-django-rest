<template>
  <section class="section">
    <div class="container">
      <div class="content">
        <div class="columns is-mobile is-vcentered">
          <div class="column is-one-quarter">
            <figure class="image is-5by4">
              <img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png" />
            </figure>
          </div>
          <div class="column">
            <div class="columns is-mobile">
              <div class="column">
                <h1 class="title">Posts</h1>
                <h2 class="subtitle">{{ user.posts_count }}</h2>
              </div>
              <div class="column">
                <h1 class="title">Followers</h1>
                <h2 class="subtitle">{{ user.followers_count }}</h2>
              </div>
              <div class="column">
                <h1 class="title">Following</h1>
                <h2 class="subtitle">{{ user.following_count }}</h2>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <h2 class="title">{{ user.username }}</h2>
        <h2 class="subtitle">{{ user.description }}</h2>
      </div>

        <div class="tile is-ancestor is-vertical">
          <div class="tile is-parent" v-for="column in posts" :key="column.index">
            <PostSmall
              v-for="post in column"
              :id="post.id"
              :key="post.id"
              :image="post.image"
              :user="post.posted_by"
            />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import PostSmall from "~/components/PostSmall";
import lodash from "lodash";

export default {
  created() {
    this.$axios
      .$get("users/" + this.user_id + "/")
      .then((response) => {
        this.user = response;
      })
      .catch((e) => {
        this.errors.push(e);
      });

    this.$axios
      .$get("users/" + this.user_id + "/posts/")
      .then((response) => {
        this.posts = lodash.chunk(response, 3);
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
  data() {
    return {
      user_id: this.$route.params.id,
      user: "",

      // Use lodash.chunk to split the array into array of multiples of 3s
      // https://dustinpfister.github.io/2017/09/13/lodash-chunk/

      posts: [],
    };
  },
  components: {
    PostSmall,
  },
};
</script>

<style scoped>
.fixed-height {
  max-height: 10px;
  color: yellow;
}
</style>