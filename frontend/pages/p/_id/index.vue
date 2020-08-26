<template>
<section class="section">
    <div class='container'>
        <PostBig 
            :id=$route.params.id 
            :img="'https://i.picsum.photos/id/' + $route.params.id +'/1200/500.jpg'"
            userid="fadhil"
        />
    </div>
</section>
</template>
<script>
import PostBig from "~/components/PostBig"

export default {
    components: {
        PostBig
    }
    
}
</script>