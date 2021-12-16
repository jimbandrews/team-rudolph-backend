from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView
from .models import Question, Answer, User
from .serializers import AnswerSerializer, QuestionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser 
from .permissions import IsQuestionAuthor

# Create your views here.



class QuestionList(ModelViewSet):
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]
        
        def perform_create(self, serializer):
            serializer.save(author=self.request.user)

        def get_permissions(self):
            """
            Instantiates and returns the list of permissions that this view requires.
            """
            if self.request.method == 'DELETE':
                permission_classes = [IsQuestionAuthor]
            else:
                permission_classes = [IsAuthenticatedOrReadOnly]
            return [permission() for permission in permission_classes]

# class QuestionList(ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class UsersAnswerList(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.filter(author_id=self.kwargs["pk"])
        return queryset

class QsAnwerList(ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs["pk"])
        serializer.save(author=self.request.user, question=question)



class AnswerDetail(UpdateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs["ans"])
        self.check_object_permissions(self.request, obj)
        return obj



class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


