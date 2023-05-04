<template>
    <div class="modal bg-black bg-opacity-75" :class="{'d-block': props.question}" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">
                        Редагування питання
                    </h5>
                    <button type="button" @click="closeModal()" class="btn-close" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @keydown.enter="editQuestion">
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
                    <button type="button" @click="closeModal()" class="btn btn-secondary">Закрити</button>
                    <button type="submit" @click="editQuestion" class="btn btn-primary">Зберегти</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {reactive, ref, watch} from 'vue'

const props = defineProps({
    question: {
        type: Object,
        default: null
    }
})
const emit = defineEmits(['addQuestion', 'editQuestion', 'close'])

const error = ref(true)

const initialQuestionForm = {
    title: '',
    subject: '',
    answer: ''
}

const questionForm = reactive({...initialQuestionForm})

watch(() => props.question, () => {
    Object.assign(questionForm, props.question)
})

watch(questionForm, () => {
    error.value = !questionForm.title || !questionForm.subject || !questionForm.answer
})

function editQuestion(event) {
  event.preventDefault()
  
  if (error.value) {
    return
  }
  
  emit('editQuestion', questionForm)

  resetForm()
}

function closeModal() {
    emit('close')
}

function resetForm() {
  Object.assign(questionForm, initialQuestionForm)
}
</script>