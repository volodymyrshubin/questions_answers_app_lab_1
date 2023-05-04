<template>
    <table class="table">
      <thead>
        <tr>
          <th colspan="5">
            <div class="text-center">Пошук</div>
          </th>
        </tr>
        <tr>
          <th><input type="text" v-model="questionForm.id" placeholder="ID" class="form-control"></th>
          <th><input type="text" v-model="questionForm.title" placeholder="Питання" class="form-control"></th>
          <th><input type="text" v-model="questionForm.subject" placeholder="Предмет" class="form-control"></th>
          <th><input type="text" v-model="questionForm.answer" placeholder="Відповідь" class="form-control"></th>
          <th></th>
        </tr>
        <tr>
          <th><a @click="orderBySelect('id', $event)" href="" :class="[props.orderBy === 'id' ? 'link-primary' : 'link-secondary']">ID</a></th>
          <th><a @click="orderBySelect('title', $event)" href="" :class="[props.orderBy === 'title' ? 'link-primary' : 'link-secondary']">Питання</a></th>
          <th><a @click="orderBySelect('subject', $event)" href="" :class="[props.orderBy === 'subject' ? 'link-primary' : 'link-secondary']">Дисципліна</a></th>
          <th><a @click="orderBySelect('answer', $event)" href="" :class="[props.orderBy === 'answer' ? 'link-primary' : 'link-secondary']">Відповідь</a></th>
          <th>Операція</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="question in props.questions">
          <td>{{ question.id }}</td>
          <td>{{ question.title }}</td>
          <td>{{ question.subject }}</td>
          <td><HiddenAnswerButton>{{ question.answer }}</HiddenAnswerButton></td>
          <td>
            <div class="row">
              <div class="col-6">
                <button @click="emit('editQuestion', question)" class="btn btn-warning form-control">Редагувати</button>
              </div>
              <div class="col-6">
                <button @click="emit('deleteQuestion', question.id)" class="btn btn-danger form-control">Видалити</button>
              </div>
            </div>
          </td>
        </tr>
        <tr v-if="!props.questions.length">
          <td colspan="5">
            <div class="text-center">Пусто!</div>
          </td>
        </tr>
      </tbody>
    </table>
</template>

<script setup>
import {reactive, watch} from 'vue'

import HiddenAnswerButton from './HiddenAnswerButton.vue';

const props = defineProps({
    questions: {
        type: Object,
        required: true,
        default: {}
    },
    orderBy: {
      type: String,
      required: false,
      default: 'id'
    }
})

const emit = defineEmits(['deleteQuestion', 'editQuestion', 'orderBySelect', 'search', 'searchReset'])

function orderBySelect(orderBy, event) {
  event.preventDefault()
  emit('orderBySelect', orderBy)
}

const questionForm = reactive({
    id: '',
    title: '',
    subject: '',
    answer: ''
})

watch(questionForm, () => emit('search', questionForm))
</script>