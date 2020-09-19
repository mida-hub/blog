<template>
  <v-container fluid>
    <div v-for="post in postList" v-bind:key="post.id">
      <div v-if="isPublic(post.is_public, post.published_at)">
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
                {{ post.published_at | moment('YYYY-MM-DD HH:mm') }}
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
  import moment from "moment"

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
    computed: {
      /**
       * 公開フラグ & 公開日付が現在日付より過去になった場合に表示する
       * @param {bool} is_public    - 公開フラグ
       * @param {Date} published_at - 公開日付
       */
      isPublic: function () {
        return function (is_public, published_at) {
          const formated_published_at = moment(published_at, 'YYYY-MM-DD HH:mm')
          const formated_current_at = moment(new Date(), 'YYYY-MM-DD HH:mm')
          
          if (is_public && formated_published_at <= formated_current_at) {
            return true
          } else {
            return false
          }
        }
      }
    },
    filters: {
      /**
       * @param {Date} value    - Date オブジェクト
       * @param {string} format - 変換したいフォーマット
       */
      moment(value, format) {
        return moment(value).format(format);
      },

    }
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
