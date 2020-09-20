<template>
  <div id="flow-list">
    <div class="flow-row">
      <div class="flow">
        <div class="flow-img">
          <img src="../assets/flow-demo.jpg" alt />
          <span>流程占位</span>
        </div>
        <div class="flow-btn-group">
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
          <div class="flow-btn">
            <img src="../assets/start-blue.png" alt />
          </div>
        </div>
      </div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
    </div>
    <div class="flow-row">
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
    </div>
    <div class="flow-row">
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
    </div>
    <div class="flow-row">
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
      <div class="flow">1111</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RightContent"
};
</script>

<style>
#flow-list {
  overflow-y: overlay;
  @apply p-1 h-full;
}

#flow-list::-webkit-scrollbar {
  width: 2px;
  @apply bg-gray-100;
}
#flow-list::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2); */
  border-radius: 10rem;
  @apply bg-gray-300;
}
#flow-list::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2); */
  border-radius: 10rem;
  @apply bg-gray-100;
}

.flow-row {
  @apply flex;
  @apply h-48;
}

.flow {
  box-shadow: 0 0 3px 1px #cbd5e0;
  @apply m-2;
  @apply rounded-lg overflow-hidden;
  @apply flex-1;
}
.flow-img {
  @apply relative;
}

.flow-img:after {
  content: "";
  position: absolute;
  width: 80px;
  height: 100%;
  top: 0;
  left: -200px;
  overflow: hidden;
  z-index: 9;
  background: -webkit-linear-gradient(
    left,
    rgba(255, 255, 255, 0) 0,
    rgba(255, 255, 255, 0.3) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: skewX(25deg);
}
.flow-img:hover:after {
  transition: left 1s ease-in-out;
  left: 500px;
}

.flow-img img {
  height: 8.5rem;
  width: 100%;
  @apply m-auto;
}
.flow-img span {
  font-weight: 700;
  font-size: 24px;
  color: #f7fafc;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.flow-btn-group {
  @apply border-t-2 border-gray-300 text-center;
}
.flow-btn {
  margin-left: 1px;
  margin-right: 1px;
  margin-top: 0.25rem;

  @apply h-full inline-block ;
}
.flow-btn:hover {
  transform: rotate(360deg);
  @apply transition-transform duration-500;
}
</style>