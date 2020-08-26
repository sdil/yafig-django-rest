<template>
  <section class="section">
      <div class="container">
            <PostBig 
                v-for="item in posts" 
                :key="item.id"
                :id="item.id" 
                :userid="item.posted_by" 
                :img="item.image"
            />
      </div>
  </section>
</template>

<script>
import PostBig from "~/components/PostBig"
import axios from "axios"

export default {
    middleware: "auth",
    components: {
        PostBig
    },
    created() {
        this.$axios.$get('posts/')
        .then(response => {
            this.posts = response
            console.log(this.posts)
        })
        .catch(e => {
        this.errors.push(e)
        })
    },
    data() {
        return{
            posts: ''
        }
    },

    // data() {
    //     return{

    //         axios.get(`https://api.themoviedb.org/3/search/movie?api_key=bb6f51bef07465653c3e553d6ab161a8&query=${name}`),

    //         posts: [
    //             {
    //                 "id": 111, 
    //                 "user": "fadhil", 
    //                 "img": "https://i.picsum.photos/id/111/1200/500.jpg",
    //                 "caption": "Hello world"
    //             },
    //             {
    //                 "id": 222, 
    //                 "user": "fadhil", 
    //                 "img": "https://i.picsum.photos/id/222/1200/500.jpg",
    //                 "caption": "Black Flies"
    //             },
    //             {
    //                 "id": 555, 
    //                 "user": "fadhil", 
    //                 "img": "https://i.picsum.photos/id/555/1200/500.jpg",
    //                 "caption": "Promise"
    //             },
    //         ]
    //     }
    // },

}
</script>

<style>

</style>