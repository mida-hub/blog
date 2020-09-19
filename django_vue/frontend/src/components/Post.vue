<template>
  <v-container fluid>
    <div v-for="post in postList" v-bind:key="post.id">
      <v-row>
        <v-card-title>
          <span class="headline">{{ post.title }}</span>
        </v-card-title>
        <v-card-text>
          {{ post.content }}
        </v-card-text>
        <v-card-subtitle>
          <p>
            <small v-for="tag in post.tags" v-bind:key="tag">
              {{ tag }}
            </small>
          </p>
          <p>
            <small>
              <em>{{ post.published_at }}</em>
            </small>
          </p>
        </v-card-subtitle>
      </v-row>
      <v-divider></v-divider>
    </div>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        postList: []
      }
    },
    mounted: function () {
      console.log('mounted')
      axios.get('/blog/posts/')
        .then((response) => {
          this.postList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
