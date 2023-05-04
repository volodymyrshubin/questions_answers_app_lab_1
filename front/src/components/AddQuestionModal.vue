<template>
    <div class="row justify-content-center">
      <div class="col-2">
        <button @click="isShow = true" class="btn btn-primary">Додати питання</button>
      </div>
    </div>

    <div class="modal bg-black bg-opacity-75" :class="{'d-block': isShow}" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">
                        Створення питання
                    </h5>
                    <button type="button" @click="closeModal()" class="btn-close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @keydown.enter="addQuestion">
                        <div class="row">
                            <div class="col">
                                <input type="text" v-model="questionForm.title" ref="firstField" placeholder="Питання" class="form-control">
                            </div>
                        </div>
                        <div class="row mt-2">
                            <div class="col">
                                <input type="text" v-model="questionForm.subject" placeholder="Предмет" class="form-control">
                            </div>
                        </div>
                        <div class="row mt-2">
                            <div class="col">
                                <input type="text" v-model="questionForm.answer" placeholder="Відповідь" class="form-control">
                            </div>
                        </div>
                    </form>
                    <div v-if="error" class="text-center">
                        <small class="text-danger">Усі поля мають бути заповнені!</small>
                    </div>
                </div>
                <div class="modal-footer">
                    <div class="form-check position-absolute start-0 ms-3">
                        <input class="form-check-input" type="checkbox" v-model="closeAfterAdding" id="flexCheckDefault">
                        <label class="form-check-label" for="flexCheckDefault">
                            Закрити після додавання
                        </label>
                    </div>
                    <button type="button" @click="closeModal()" class="btn btn-secondary">Закрити</button>
                    <button type="submit" @click="addQuestion" class="btn btn-primary">Зберегти</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {reactive, ref, watch} from 'vue'

const emit = defineEmits(['addQuestion'])

const isShow = ref(false)
const error = ref(true)
const closeAfterAdding = ref(true)

const initialQuestionForm = {
    title: '',
    subject: '',
    answer: ''
}

const questionForm = reactive({...initialQuestionForm})

const firstField = ref(null)

watch(questionForm, () => {
    error.value = !questionForm.title || !questionForm.subject || !questionForm.answer
})

function addQuestion(event) {
  event.preventDefault()
  
  if (error.value) {
    return
  }
  
  emit('addQuestion', questionForm)
  resetForm()

  if (closeAfterAdding.value){
      closeModal()
      return
  }

  firstField.value.focus()
}

function closeModal() {
    isShow.value = false
    resetForm()
}

function resetForm() {
  Object.assign(questionForm, initialQuestionForm)
}
</script>