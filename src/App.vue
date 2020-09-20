<template>
  <div id="app" class="flex p-2">
    <div id="flow-left-menu"><LeftMenu /></div>
    <div id="flow-right-content"><RightContent /></div>
  </div>
</template>

<script>
import LeftMenu from './components/LeftMenu'
import RightContent from './components/RightContent'

export default {
  name: "App",
  components: {
    LeftMenu,
    RightContent
  }
};
</script>

<style>
#app {
  @apply bg-gray-100;
  @apply h-full;
}
#flow-left-menu {
  /* border-radius: 0.5rem; */
  width: 15rem;
  box-shadow: 0 0 3px 1px #cbd5e0;
  @apply flex-none;
  @apply rounded-lg;
  @apply mr-3 px-2 py-1;
}
#flow-right-content {
  box-shadow: 0 0 3px 1px #cbd5e0;
  @apply flex-1;
  @apply rounded-lg;
  @apply mr-2;
}
</style>