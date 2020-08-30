<template>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h2 class="title has-text-centered">Register!</h2>

          <Notification :message="error" v-if="error" />

          <form method="post" @submit.prevent="register">

            <div class="field">
              <label class="label">Email</label>
              <div class="control">
                <input type="enauk" class="input" name="email" v-model="email" required />
              </div>
            </div>

            <div class="field">
                          <label class='label'>Username</label>
                          <div class="control">
                              <input type="text" class="input" name="username" v-model="username" required>
                          </div>
            </div>

            <div class="field">
              <label class="label">Password</label>
              <div class="control">
                <input type="password" class="input" name="password" v-model="password" required />
              </div>
            </div>

            <div class="field">
              <button type="submit" class="button is-dark is-fullwidth">Register</button>
            </div>
          </form>

          <div class="has-text-centered" style="margin-top:20px">
            Already got an account?
            <nuxt-link to="/login">Login</nuxt-link>
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
  middleware: "guest",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async register() {
      try {
        await this.$axios.post("users/register/", {
          email: this.email,
          username: this.username,
          password: this.password,
        });
        
        this.$router.push("/feed");
      } catch (e) {
        this.error = e.response.data.detail;
      }
    },
  },
};
</script>