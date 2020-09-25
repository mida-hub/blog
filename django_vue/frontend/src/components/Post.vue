<template>
  <v-container fluid>
    <div v-for="post in postList" v-bind:key="post.id">
      <div v-if="post.is_display || token">
        <v-row>
          <v-card-title>
            <span class="headline">
              <router-link
                v-bind:to="{name: 'postDetail', params: {postId: post.id}}"
                class="post-link"
              >
                {{ post.with_prefix_title }}  
              </router-link>
            </span>
          </v-card-title>
          <v-card-text>
            <span v-html="post.abstract"></span>
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
        <v-divider/>
      </div>
    </div>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        postList: [],
        token: null
      }
    },
    methods: {
      getEndpoint: function (tagId) {
        if( tagId === undefined){
          return this.$apiPath + '/posts/'
        } else {
          return this.$apiPath + '/posts/tags/' + tagId + '/'
        } 
      },
      getPostList: function (tagId) {
        const endpoint = this.getEndpoint(tagId)
        console.log('post mounted')
        console.log(endpoint)
        axios.get(endpoint)
        .then((response) => {
          this.postList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    created: function () {
      const tagId = this.$route.params.tagId
      this.getPostList(tagId)
      this.token = this.$store.getters.getAuthToken
    },
    watch: {
      $route (to) {
        const tagId = to.params.tagId
        this.getPostList(tagId)
        this.token = this.$store.getters.getAuthToken
      }
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
