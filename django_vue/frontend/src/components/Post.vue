<template>
  <v-container fluid>
                <router-link
              style="text-decoration: none; color: inherit;"
              to="/post"
            >
              post
            </router-link>
    <div v-for="post in postList" v-bind:key="post.id">
      <div v-if="isPublic(post.is_public, post.published_at)">
        <v-row>
          <v-card-title>
            <span class="headline">{{ post.title }}</span>
          </v-card-title>
          <v-card-text>
            {{ post.content | summaryContent }}
          </v-card-text>
          <v-card-subtitle>
            <p>
              <small>
                {{ post.published_at | moment('YYYY-MM-DD HH:mm') }}
              </small>
              <small v-for="tag in post.tags" v-bind:key="tag">
                [{{ getTagName(tag, tagList) }}]
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
        postList: [],
        tagList: []
      }
    },
    created: function () {
      console.log('post-tag mounted')
      axios.get('/blog/tags/')
        .then((response) => {
          this.tagList = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      console.log('post mounted')
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
      },
      /**
       * タグIDからタグ名に変換する
       * @param {int} tag        - タグID
       * @param [{json}] tagList - タグ一覧 [json]
       */
      getTagName: function () {
        return function (tag, tagList) {
          const tagItem = tagList.find((item) => item.id === tag)
          return tagItem.name
        }
      }
    },
    filters: {
      /**
       * @param {Date} value    - Date オブジェクト
       * @param {string} format - 変換したいフォーマット
       */
      moment (value, format) {
        return moment(value).format(format);
      },
      /**
       * 記事一覧で表示する見出しコンテンツ
       * 一定以上の文字列長の場合は切り出す
       * @param {string} content - 記事のコンテンツ
       */
      summaryContent: function (content) {
        const cutLength = 80
        if (content.length <= cutLength) {
          return content
        } else {
          return content.substring(cutLength, -1).concat('......')
        }
      }
    }
  }
</script>

<style scoped>
</style>
