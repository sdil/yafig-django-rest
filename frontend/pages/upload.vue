<template>
  <section class="section">
    <div class="container">
      <div class="content">
        <h1>Upload new Photo</h1>
        <div v-if="file == null">
          <b-field>
            <b-upload v-model="file" drag-drop native @input="onFileChange">
              <section class="section">
                <div class="content has-text-centered">
                  <p>
                    <b-icon icon="upload" size="is-large"></b-icon>
                  </p>
                  <p>Drop your files here or click to upload</p>
                </div>
              </section>
            </b-upload>
          </b-field>
        </div>

        <div v-else>
          <div id="preview">
            <img :src="url" />
          </div>

          <b-field label="Caption">
            <b-input v-model="caption" rounded></b-input>
          </b-field>

          <b-field label="Tags">
            <b-input placeholder="Cat" rounded></b-input>
          </b-field>

          <b-button type="is-primary" rounded @click="upload">Upload</b-button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  middleware: "auth",
  methods: {
    onFileChange(e) {
      console.log("file-change");
      console.log(e);
      this.url = URL.createObjectURL(e);
    },
    upload() {
      var formData = new FormData();
      formData.append("image", this.file);
      formData.append("caption", this.caption);

      this.$axios
        .post("/posts/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .catch(function (e) {
          console.log("failed");
          console.log(e);
        });

        this.$router.push("/feed");
    },
  },
  data() {
    return {
      url: null,
      file: null,
      caption: "",
    };
  },
};
</script>

<style scoped>
#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>