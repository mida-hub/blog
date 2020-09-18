<template>
<div id="app">
  <MyHeader></MyHeader>
  <v-container fluid grid-list-md>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap align-center>
        <v-flex v-for="entry in entryList" v-bind:key="entry.id">
          <v-card>
            <v-card-title>
              <span class="headline">{{ entry.title }}</span>
            </v-card-title>
            <v-card-text>
              <blockquote>
                {{ entry.contnt }}
                <footer>
                  <small>
                    <em>&mdash;{{ entry.date }}</em>
                  </small>
                </footer>
              </blockquote>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
  <MyFooter></MyFooter>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'
import MyHeader from '@/components/Header'
import MyFooter from '@/components/Footer'

export default {
  data () {
    return {
      entryList: []
    }
  },
  mounted: function () {
    console.log('mounted')
    // APIを叩く。
    // 開発サーバで動作中はちゃんとDjangoの8000番ポートを叩いてくれます。
    axios.get('/api/entries/')
      .then((response) => {
        this.entryList = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  components: {
    MyHeader,
    MyFooter
  }
}
</script>
