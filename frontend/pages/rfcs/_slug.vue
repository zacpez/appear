<template>
  <article class="content-container">
    <h1>{{ page.title }}</h1>
    <nuxt-content :document="page" />
  </article>
</template>

<script>
export default {
  async asyncData({ $content, params }) {
    const page = await $content('rfcs', params.slug).fetch()

    return {
      page,
    }
  },
}
</script>
