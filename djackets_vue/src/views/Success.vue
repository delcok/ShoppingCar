<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="title">Thank you</div>

      <p>Your order will be processed within 48 hours</p>
    </div>
  </div>

</template>

<script>
export default {
  name: "Success",
  mounted() {
    document.title = 'Success | Djackets'
  }
}
</script>

<style scoped>

</style>