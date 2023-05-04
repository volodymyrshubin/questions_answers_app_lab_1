<template>
  <div class="container">
    <QuestionsTable 
      :questions="questionsSearched" 
      @addQuestion="addQuestion" 
      @editQuestion="selectedToEditQuestion = $event" 
      @deleteQuestion="deleteQuestion" 
      @orderBySelect="sortQuestions" 
      :orderBy="sortOrderBy"

      @search="searchForm = $event" 
      @searchReset="fetchQuestions()"
    />
    <AddQuestionModal @addQuestion="addQuestion"/>
    <EditQuestionModal @editQuestion="editQuestion" @close="selectedToEditQuestion = null" :question="selectedToEditQuestion"/>
  </div>
</template>

<script setup>
import api from './api'
import {ref, computed} from 'vue'
import QuestionsTable from './components/QuestionsTable.vue';
import AddQuestionModal from './components/AddQuestionModal.vue';
import EditQuestionModal from './components/EditQuestionModal.vue';

const questions = ref([])

const sortOrderBy = ref('id')
const searchForm = ref({})

const selectedToEditQuestion = ref(null)

const questionsSearched = computed(() => {
  return [...questionsSorted.value].filter(question => {
    const conditions = [true]

    conditions.push(!searchForm.value.id || question.id.toString().includes(searchForm.value.id))
    conditions.push(!searchForm.value.title || question.title.toLowerCase().includes(searchForm.value.title.toLowerCase()))
    conditions.push(!searchForm.value.subject || question.subject.toLowerCase().includes(searchForm.value.subject.toLowerCase()))
    conditions.push(!searchForm.value.answer || question.answer.toLowerCase().includes(searchForm.value.answer.toLowerCase()))

    return conditions.every(condition => condition)
  })
})

const questionsSorted = computed(() => {
  return [...questions.value].sort((a, b) => a[sortOrderBy.value].toString().localeCompare(b[sortOrderBy.value].toString(), undefined, { numeric: true }))
})

function sortQuestions(orderBy) {
  if (sortOrderBy.value === orderBy) {
    sortOrderBy.value = 'id'
    return
  }
  sortOrderBy.value = orderBy
}

function fetchQuestions() {
  api.get('questions').then(response => {
    questions.value = response.data
  })
}

function addQuestion(data) {
  api.post('questions/', data).then(response => {
    questions.value.push(response.data)
  })
}

function editQuestion(data) {
  api.put(`questions/${data.id}/`, data).then(response => {
    selectedToEditQuestion.value = null
    fetchQuestions()
  })
}

function deleteQuestion(id) {
  api.delete(`questions/${id}`).then(response => {
    fetchQuestions()
  })
}

fetchQuestions()

</script>
