from abc import abstractmethod

from AnnotatedSentence.ViewLayerType import ViewLayerType
from NamedEntityRecognition.AutoNER import AutoNER

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.Condition.IsTransferable import IsTransferable
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class TreeAutoNER(AutoNER):

    second_language: ViewLayerType

    @abstractmethod
    def autoDetectPerson(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectLocation(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectOrganization(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectMoney(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectTime(self, parseTree: ParseTreeDrawable):
        pass

    def __init__(self, secondLanguage: ViewLayerType):
        self.second_language = secondLanguage

    def autoNER(self, parseTree: ParseTreeDrawable):
        self.autoDetectPerson(parseTree)
        self.autoDetectLocation(parseTree)
        self.autoDetectOrganization(parseTree)
        self.autoDetectMoney(parseTree)
        self.autoDetectTime(parseTree)
        node_drawable_collector = NodeDrawableCollector(parseTree.getRoot(), IsTransferable(self.second_language))
        leaf_list = node_drawable_collector.collect()
        for parse_node in leaf_list:
            if isinstance(parse_node, ParseNodeDrawable) and not parse_node.layerExists(ViewLayerType.NER):
                parse_node.getLayerInfo().setLayerData(ViewLayerType.NER, "NONE")
        parseTree.save()
