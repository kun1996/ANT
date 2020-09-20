<template>
  <ul id="menu-group">
    <li>
      <div class="menu-level-1">
        <div class="menu">
          <span>菜单</span>
        </div>
        <div class="overflow-hidden">
          <div class="menu-level-2">
            <div class="menu">子菜单</div>
            <div class="menu">子菜单</div>
            <div class="menu">子菜单</div>
          </div>
        </div>
      </div>
    </li>
    <li>
      <div>3</div>
    </li>
    <li>
      <div>3</div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "LeftMenu"
};
</script>

<style>
#menu-group {
  @apply list-none;
}
.menu-level-1 > .menu {
  font-size: 18px;
}
.menu-level-1 > .menu::before {
  content: "\00A0\00A0\00A0\00A0\00A0\00A0";
  display: inline-block;
  width: 30px;
  height: 30px;
  background: url("../assets/start-blue.png") no-repeat;
}
.menu-level-1 > .menu:hover::before {
  transition: transform 0.5s ease-in-out;
  transform: rotate(90deg);
}

.menu-level-2 {
  display: none;
}

.menu-level-2:active {
  display: block;
  animation: fadeio 1s;
}
.menu-level-2 > .menu {
  padding-left: 30px;
}
.menu-level-2 > .menu:hover {
  background-color: #4299e1;
  color: #f5f5f5;
  transition: all 0.5s ease-in-out;
}

.menu {
  border-bottom: 1px solid #cbd5e0;
  display: block;
}
.menu span {
  display: inline-block;
  padding-left: 2px;
  height: 30px;
  line-height: 30px;
  vertical-align: middle;
  font-weight: 500;
}

@keyframes fadeio {
  /*设置内容由显示变为隐藏*/
  0% {
    opacity: 0;
    transform: translate(0, -100%);
  }
  100% {
    opacity: 1;
    transform: translate(0, 0);
  }
}
</style>