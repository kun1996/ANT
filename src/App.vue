<template>
  <div id="app" class="flex p-2">
    <div id="flow-left-menu">
      <LeftMenu />
    </div>
    <div id="flow-right-content">
      <RightContent />
    </div>
    <div id="flow-chart">
      <FlowChart />
    </div>
  </div>
</template>

<script>
import LeftMenu from "./components/LeftMenu";
import RightContent from "./components/RightContent";
import FlowChart from "./components/FlowChart";

export default {
  name: "App",
  components: {
    LeftMenu,
    RightContent,
    FlowChart
  }
};
</script>

<style>
#app {
  @apply bg-gray-100;
  @apply h-full;
  @apply relative;
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
#flow-chart {
  box-shadow: 0 0 3px 1px #cbd5e0;
  @apply absolute;
  @apply rounded-lg;
  overflow: overlay;
  background-color: #f7fafc;
  height: 80%;
  width: 80%;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

#flow-chart::-webkit-scrollbar {
  width: 2px;
  height: 2px;
  @apply bg-gray-100;
}
#flow-chart::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2); */
  border-radius: 10rem;
  @apply bg-gray-300;
}
#flow-chart::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2); */
  border-radius: 10rem;
  @apply bg-gray-100;
}
</style>