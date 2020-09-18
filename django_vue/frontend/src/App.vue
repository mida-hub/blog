<template>
  <div id="app">
    <Header></Header>
    <Main></Main>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Main from '@/components/Main'
// import Category from '@/components/Category'
// import Tag from '@/components/Tag'
import Footer from '@/components/Footer'

export default {
  components: {
    Header,
    Main,
    // Category,
    // Tag,
    Footer
  }
}
</script>
