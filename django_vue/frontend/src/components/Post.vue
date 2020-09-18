<template>
  <v-container fluid grid-list-md>
    <v-slide-y-transition mode="out-in">
      <v-layout column wrap align-center>
        <v-flex v-for="post in postList" v-bind:key="post.id">
          <v-card outlined>
            <v-card-title>
              <span class="headline">{{ post.title }}</span>
            </v-card-title>
            <v-card-text>
              {{ post.content }}
            </v-card-text>
            <v-card-subtitle>
              <small>
                <em>{{ post.updated_at }}</em>
              </small>
            </v-card-subtitle>
            <v-card-subtitle>
              <v-chip v-for="tag in post.tags" v-bind:key="tag">
                {{ tag }}
              </v-chip>
            </v-card-subtitle>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
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
