<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  components: {
    Header,
    Footer
  }
}
</script>

<style>
@import 'statics/normalize.css';

#app {
  font-family: 'sans-serif', 'Helvetica';
}
</style>
