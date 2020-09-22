<template>
  <v-container fluid>
    <div v-for="post in postList" v-bind:key="post.id">
      <div v-if="post.is_display">
        <v-row>
          <v-card-title>
            <span class="headline">
              <router-link
                v-bind:to="{name: 'postDetail', params: {postId: post.id}}"
                class="post-link"
              >
                {{ post.title }}  
              </router-link>
            </span>
          </v-card-title>
          <v-card-text>
            <span v-html="post.summarized_content"></span>
          </v-card-text>
          <v-card-subtitle>
            <p>
              <small>
                {{ post.formatted_published_at }}
              </small>
              <small v-for="tag in post.tags" v-bind:key="tag.id">
                [{{ tag.name }}]
              </small>
            </p>
          </v-card-subtitle>
        </v-row>
        <v-divider></v-divider>
      </div>
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
    created: function () {
      console.log('post mounted')
      axios.get('/blog-api/posts/')
        .then((response) => {
          this.postList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
</script>

<style scoped>
  .post-link {
    text-decoration: none;
    color: inherit;
  }
  .post-link:hover{
    padding-bottom: 3px;
    border-bottom: 1px solid;
    color: dimgray;
  }
</style>
