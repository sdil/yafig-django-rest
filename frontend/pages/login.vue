<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h2 class="title has-text-centered">Welcome back!</h2>

          <Notification :message="this.error" v-if="this.error" />

          <form method="post" @submit.prevent="login">
            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input type="email" class="input" name="email" v-model="email" required />
              </div>
            </div>

            <div class="field">
              <label class="label">Password</label>
              <div class="control">
                <input type="password" class="input" name="password" v-model="password" required />
              </div>
            </div>

            <div class="field">
              <button type="submit" class="button is-dark is-fullwidth">Login</button>
            </div>
          </form>

          <div class="has-text-centered" style="margin-top:20px">
            Don't have an account?
            <nuxt-link to="/register">Register</nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Notification from "~/components/Notification";

export default {
  components: {
    Notification,
  },
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith("local", {
          data: {
            username: this.email,
            password: this.password,
          },
        });
        this.$router.push("/feed");
      } catch (e) {
        this.error = e.response.data.detail;
        console.log(this.error);
      }
    },
  },
};
</script>

<style>
</style>