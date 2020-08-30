<template>
  <b-navbar>
    <template slot="brand" v-if="isAuthenticated">
      <b-navbar-item tag="router-link" to="/feed">
        <img src="~/assets/logo.png" alt="Yet Another Free (OSS) Instagram-clone" />
      </b-navbar-item>
    </template>

    <template slot="brand" v-else>
      <b-navbar-item tag="router-link" to="/">
        <img src="~/assets/logo.png" alt="Yet Another Free (OSS) Instagram-clone" />
      </b-navbar-item>
    </template>

    <template slot="start">
      <b-navbar-item tag="router-link" to="/search" v-if="isAuthenticated">Search</b-navbar-item>
      <b-navbar-item tag="router-link" to="/wth">WTH is this?</b-navbar-item>
    </template>

    <template slot="end" v-if="isAuthenticated">
      <b-navbar-item tag="div">
        <div class="buttons">
          <nuxt-link to="/upload" class="button is-light">Upload Photo</nuxt-link>
          <nuxt-link :to="'/u/' + this.$auth.user" class="button is-primary">
            <strong>My Profile</strong>
          </nuxt-link>
          <a class="button is-light" @click="logout">Log out</a>
        </div>
      </b-navbar-item>
    </template>

    <template slot="end" v-else>
      <b-navbar-item tag="div">
        <div class="buttons">
          <nuxt-link to="/register" class="button is-success">
            <strong>Sign up</strong>
          </nuxt-link>
          <nuxt-link to="/login" class="button is-light">Log in</nuxt-link>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated", "loggedInUser"]),
  },
  methods: {
    async logout() {
      await this.$auth.logout();
    },
  },
};
</script>

<style>
</style>