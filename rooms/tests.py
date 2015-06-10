from django.test import TestCase
from rooms import models
from rooms.api import renderers, serializers, views
from rest_framework.utils.serializer_helpers import ReturnList
from operator import itemgetter
import json


class JSONRendererTestCase(TestCase):

    fixtures = ['room', 'building']

    @classmethod
    def setUpTestData(cls):
        cls.renderer = renderers.JSONRenderer()
        cls.room_queryset = models.Room.objects.all()
        cls.building_queryset = models.Building.objects.all()

    def test_render_room_list(self):

        actual_room_list = self._render_list(
            queryset=self.room_queryset,
            renderer=self.renderer,
            serializer_class=serializers.RoomSerializer,
            view=views.RoomViewSet()
        )
        serializable_list = serializers.RoomSerializer(list(self.room_queryset), many=True)
        expected_room_list = json.dumps({'rooms': serializable_list.data})

        self.assertEqual(actual_room_list, expected_room_list)

    def test_render_single_room(self):

        for room in self.room_queryset:

            actual_room = self._render_object(
                serializer_class=serializers.RoomSerializer,
                obj=room,
                renderer=self.renderer,
                view=views.RoomViewSet()
            )

            room_serializer = serializers.RoomSerializer(room)
            expected_room = json.dumps({'room': room_serializer.data})

            self.assertEqual(actual_room, expected_room)

    def test_render_building_list(self):

        actual_building_list = self._render_list(
            queryset=self.building_queryset,
            renderer=self.renderer,
            serializer_class=serializers.BuildingSerializer,
            view=views.BuildingViewSet()
        )
        serializable_list = serializers.BuildingSerializer(list(self.building_queryset), many=True)
        expected_building_list = json.dumps({'buildings': serializable_list.data})

        self.assertEqual(actual_building_list, expected_building_list)

    def test_render_single_building(self):

        for building in self.building_queryset:

            actual_building = self._render_object(
                serializer_class=serializers.BuildingSerializer,
                obj=building,
                renderer=self.renderer,
                view=views.BuildingViewSet()
            )

            building_serializer = serializers.BuildingSerializer(building)
            expected_building = json.dumps({'room': building_serializer.data})

            self.assertEqual(actual_building, expected_building)

    def _render_list(self, **kwargs):

        serializer_class = kwargs.pop('serializer_class')
        queryset = kwargs.pop('queryset')
        renderer = kwargs.pop('renderer')
        view = kwargs.pop('view')

        serializer = serializer_class(list(queryset), many=True)
        obj_list = serializer.data

        return renderer.render(obj_list, renderer_context={'view': view})

    def _render_object(self, **kwargs):

        serializer_class = kwargs.pop('serializer_class')
        obj = kwargs.pop('obj')
        renderer = kwargs.pop('renderer')
        view = kwargs.pop('view')

        serializer = serializer_class(obj)
        return renderer.render(serializer.data, renderer_context={'view': view})
