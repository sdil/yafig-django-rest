<template>
      <b-navbar>
        <template slot="brand" v-if="isAuthenticated">
            <b-navbar-item tag="router-link" to="/feed">
                <img
                    src="~/assets/logo.png"
                    alt="Yet Another Free (OSS) Instagram-clone"
                >
            </b-navbar-item>
        </template>

        <template slot="brand" v-else>
            <b-navbar-item tag="router-link" to="/">
                <img
                    src="~/assets/logo.png"
                    alt="Yet Another Free (OSS) Instagram-clone"
                >
            </b-navbar-item>
        </template>

        <template slot="start">
            <nuxt-link to="/search" v-if="isAuthenticated"><b-navbar-item>
                Search
            </b-navbar-item></nuxt-link>
            <nuxt-link to="/wth"><b-navbar-item>
              WTH is this?
            </b-navbar-item></nuxt-link>
        </template>

        <template slot="end" v-if="isAuthenticated">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <nuxt-link to="upload">
                      <a class="button is-light">
                          New Photo
                      </a></nuxt-link>
                    <nuxt-link :to="'/u/' + this.$auth.user">
                      <a class="button is-primary">
                          <strong>My Profile</strong>
                      </a></nuxt-link>
                    <a class="button is-light" @click="logout">
                        Log out
                    </a>
                </div>
            </b-navbar-item>
        </template>

        <template slot="end" v-else>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <nuxt-link to="/register">
                      <a class="button is-success">
                          <strong>Sign up</strong>
                      </a></nuxt-link>
                    <a class="button is-light">
                      <nuxt-link to="/login">
                        Log in
                      </nuxt-link>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser'])
    },
    methods: {
        async logout() {
            await this.$auth.logout();
        }
    }
}
</script>

<style>
</style>