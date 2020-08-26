<template>
<section class="section">
      <div class="container">
          <div class="content">
              <div class="columns is-mobile is-vcentered">
                <div class="column is-one-quarter">
                    <figure class="image is-5by4">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
                    </figure>
                </div>
                <div class="column ">
                    <div class="columns is-mobile">
                        <div class="column">
                            <h1 class="title">Posts</h1>
                            <h2 class="subtitle">36</h2>
                        </div>
                        <div class="column">
                            <h1 class="title">Followers</h1>
                            <h2 class="subtitle">36</h2>
                        </div>
                        <div class="column">
                            <h1 class="title">Following</h1>
                            <h2 class="subtitle">36</h2>
                        </div>
                    </div>
                </div>
            </div>
          </div>
          
          <div>
                <h2 class="title">{{ $route.params.id }}</h2>
                <h2 class="subtitle">She's my pride and joy</h2>
          </div>

        <div class="tile is-ancestor is-vertical">
            <div class="tile is-parent" v-for="column in posts" :key="column">
                <PostSmall
                    v-for="post in column"
                    :id="post.id"
                    :key="post.id" 
                    :img="post.img" 
                    :userid="post.userid"
                />
            </div>
        </div>

      </div>
  </section>
</template>

<script>
import PostSmall from "~/components/PostSmall"
import lodash from "lodash"


export default {
    data() {
        return {
            // Use lodash.chunk to split the array into array of multiples of 3s
            // https://dustinpfister.github.io/2017/09/13/lodash-chunk/
            posts: lodash.chunk([
                {"id": 201, "user": "fadhil", "img": "https://i.picsum.photos/id/201/1200/500.jpg"},
                {"id": 202, "user": "fadhil", "img": "https://i.picsum.photos/id/202/1200/500.jpg"},
                {"id": 203, "user": "fadhil", "img": "https://i.picsum.photos/id/203/1200/500.jpg"}
            ], 3),
        }
    },
    middleware: "auth",
    components: {
        PostSmall
    }
}
</script>

<style>

</style>