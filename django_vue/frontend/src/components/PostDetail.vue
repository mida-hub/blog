<template>
  <v-container fluid>
    <v-row>
      <v-card outlined width="100%">
        <div v-if="isNotDisplay">
          <v-card-title>
            This request is invalid.
          </v-card-title>
        </div>
        <div v-else>
          <v-card-title>
            <h1>
              {{ postDetail.title }}
            </h1>
          </v-card-title>
          <v-card-subtitle style="color: rgba(0, 0, 0, 0.87);">
            <v-chip-group column>
              <v-chip label @click="tagFilter(tag.id)" v-for="tag in postDetail.tags" v-bind:key="tag.id">
                {{ tag.name }}
              </v-chip>
            </v-chip-group>
            <p class="p-margin">
              {{ postDetail.formatted_published_at }}
            </p>
          <div class="divider"></div>
          </v-card-subtitle>
          <v-card-text>
            <markdown-it-vue class="md-body" :content="markdownText" />
          </v-card-text>
        </div>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import MarkdownItVue from 'markdown-it-vue'
  import 'markdown-it-vue/dist/markdown-it-vue.css'

  export default {
    components: {
      MarkdownItVue
    },
    data () {
      return {
        postDetail: [],
        markdownText: '',
        isNotDisplay: false,
        token: null
      }
    },
    methods: {
      forceRedirect: function () {
        setTimeout(function () {
              location.href = '/'
            }, 1000);
      },
      tagFilter: function ( tagId ) {
        this.$router.push({ name: 'tagFilter', params: { tagId: tagId } })
      }
    },
    created: function () {
      this.token = this.$store.getters.getAuthToken
      console.log('post mounted')
      const postId = this.$route.params.postId
      axios.get(this.$apiPath + '/posts/' + postId + '/')
        .then((response) => {
          this.postDetail = response.data
          this.markdownText = this.postDetail.abstract_content
          console.log(this.token)
          // ToDo token が有効か判定する
          //   is_display が false のときに下記メソッドを実行して
          //   エラーのときは token に null を強制的にセットする
          // console.log('/dummy_auth/')
          // axios.get(this.$apiPath + '/dummy_auth/', {
          //   headers: {
          //     Authorization: `JWT ${this.token}`,
          //   }
          // })
          // .then((response) => {
          //   console.log('認証')
          //   console.log(response)
          // })
          // .catch((error) => {
          //   console.log('エラー')
          //   console.log(error)
          // })
          if ( !this.postDetail.is_display && !this.token) {
            this.isNotDisplay = true
            // 非公開のため1秒後にリダイレクト
            this.forceRedirect()
          }
        })
        .catch((error) => {
          console.log(error)
          this.isNotDisplay = true
          // Not Found のため1秒後にリダイレクト
          this.forceRedirect()
        })
    },
  }
</script>

<style scoped>
  .detail-right{
    text-align: right;
  }
  .p-margin{
    margin-top: 14px;
    margin-bottom: 14px;
  }
  .divider{
    border-bottom: 1px solid;
  }
</style>

<style>
  img {
    max-width: 100%;
    height: auto;
  }

</style>
