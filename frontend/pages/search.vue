<template>
    <section class="section">
        <div class="container">
            <b-field label="Search your fav pics">
                <b-autocomplete
                    :data="data"
                    placeholder="e.g. ragdoll cat"
                    field="title"
                    :loading="isFetching"
                    @typing="getAsyncData"
                    @select="option => selected = option">

                    <template slot-scope="props">
                        <div class="media">
                            <div class="media-left">
                                <img width="32" :src="`https://image.tmdb.org/t/p/w500/${props.option.poster_path}`">
                            </div>
                            <div class="media-content">
                                {{ props.option.title }}
                                <br>
                                <small>
                                    Released at {{ props.option.release_date }},
                                    rated <b>{{ props.option.vote_average }}</b>
                                </small>
                            </div>
                        </div>
                    </template>
                </b-autocomplete>
            </b-field>


            <hr>
            <div class="tile is-ancestor is-vertical">
                <div class="tile is-parent" v-for="column in posts" :key="column">
                    <PostSmall
                        v-for="post in column"
                        :id="post.id"
                        :key="post.id" 
                        :image="post.image" 
                        :userid="post.userid"
                    />
                </div>
            </div>
            
        </div>
    </section>
</template>

<script>
import PostSmall from "~/components/PostSmall"
import debounce from 'lodash/debounce'
import lodash from "lodash"
import axios from "axios"

export default {
    data() {
        return{
            // Use lodash.chunk to split the array into array of multiples of 3s
            // https://dustinpfister.github.io/2017/09/13/lodash-chunk/
            posts: lodash.chunk([
                {"id": 100, "user": "fadhil", "img": "https://i.picsum.photos/id/100/1200/500.jpg"},
                {"id": 101, "user": "fadhil", "img": "https://i.picsum.photos/id/101/1200/500.jpg"},
                {"id": 102, "user": "fadhil", "img": "https://i.picsum.photos/id/102/1200/500.jpg"},
                {"id": 103, "user": "fadhil", "img": "https://i.picsum.photos/id/103/1200/500.jpg"}
            ], 3),
            post_columns: [],
            data: [],
            selected: null,
            isFetching: false,
        }
    },
    methods: {
        getAsyncData: debounce(function (name) {
                if (!name.length) {
                    this.data = []
                    return
                }
                this.isFetching = true
                axios.get(`https://api.themoviedb.org/3/search/movie?api_key=bb6f51bef07465653c3e553d6ab161a8&query=${name}`)
                    .then(({ data }) => {
                        this.data = []
                        data.results.forEach((item) => this.data.push(item))
                    })
                    .catch((error) => {
                        this.data = []
                        throw error
                    })
                    .finally(() => {
                        this.isFetching = false
                    })
            }, 500),
    },
    middleware: "auth",
    components: {
        PostSmall
    }
}
</script>

<style>
</style>