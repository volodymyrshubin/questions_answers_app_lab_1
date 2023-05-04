<template>
    <button v-if="!showAnswer" @click="showAnswer = true" class="btn btn-secondary">Показати відповідь</button>
    <span v-else><slot>Пусто!</slot></span>
</template>

<script setup>
import {ref} from 'vue'
const showAnswer = ref(false)
</script>