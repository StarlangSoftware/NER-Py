# Named Entity Recognition

## Task Definition

In named entity recognition, one tries to find the strings within a text that correspond to proper names (excluding TIME and MONEY) and classify the type of entity denoted by these strings. The problem is difficult partly due to the ambiguity in sentence segmentation; one needs to extract which words belong to a named entity, and which not. Another difficulty occurs when some word may be used as a name of either a person, an organization or a location. For example, Deniz may be used as the name of a person, or - within a compound - it can refer to a location Marmara Denizi 'Marmara Sea', or an organization Deniz Taşımacılık 'Deniz Transportation'.

The standard approach for NER is a word-by-word classification, where the classifier is trained to label the words in the text with tags that indicate the presence of particular kinds of named entities. After giving the class labels (named entity tags) to our training data, the next step is to select a group of features to discriminate different named entities for each input word.

[<sub>ORG</sub> Türk Hava Yolları] bu [<sub>TIME</sub> Pazartesi'den] itibaren [<sub>LOC</sub> İstanbul] [<sub>LOC</sub> Ankara] hattı için indirimli satışlarını [<sub>MONEY</sub> 90 TL'den] başlatacağını açıkladı.

[<sub>ORG</sub> Turkish Airlines] announced that from this [<sub>TIME</sub> Monday] on it will start its discounted fares of [<sub>MONEY</sub> 90TL] for [<sub>LOC</sub> İstanbul] [<sub>LOC</sub> Ankara] route.

See the Table below for typical generic named entity types.

|Tag|Sample Categories|
|---|---|
|PERSON|people, characters|
|ORGANIZATION|companies, teams|
|LOCATION|regions, mountains, seas|
|TIME|time expressions|
|MONEY|monetarial expressions|

## Data Annotation

### Preparation

1. Collect a set of sentences to annotate. 
2. Each sentence in the collection must be named as xxxx.yyyyy in increasing order. For example, the first sentence to be annotated will be 0001.train, the second 0002.train, etc.
3. Put the sentences in the same folder such as *Turkish-Phrase*.
4. Build the [Java](https://github.com/starlangsoftware/NER) project and put the generated sentence-ner.jar file into another folder such as *Program*.
5. Put *Turkish-Phrase* and *Program* folders into a parent folder.

### Annotation

1. Open sentence-ner.jar file.
2. Wait until the data load message is displayed.
3. Click Open button in the Project menu.
4. Choose a file for annotation from the folder *Turkish-Phrase*.  
5. For each word in the sentence, click the word, and choose approprite entity tag from PERSON, ORGANIZATION, LOCATION, TIME, or MONEY tags.
6. Click one of the next buttons to go to other files.

## Classification DataSet Generation

After annotating sentences, you can use [DataGenerator](https://github.com/starlangsoftware/DataGenerator-Py) package to generate classification dataset for the Named Entity Recognition task.

## Generation of ML Models

After generating the classification dataset as above, one can use the [Classification](https://github.com/starlangsoftware/Classification-Py) package to generate machine learning models for the Named Entity Recognition task.

Simple Web Interface
============
[Link 1](http://104.247.163.162/nlptoolkit/turkish-named-entity-recognition.html) [Link 2](https://starlangsoftware.github.io/nlptoolkit-web-simple/turkish-named-entity-recognition.html)

Video Lectures
============

[<img src=https://github.com/StarlangSoftware/NER/blob/master/video.jpg width="50%">](https://youtu.be/4pxdvP_Rfd8)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/NER-Cy), [Java](https://github.com/starlangsoftware/NER), [C++](https://github.com/starlangsoftware/NER-CPP), [Swift](https://github.com/starlangsoftware/NER-Swift), [Js](https://github.com/starlangsoftware/NER-Js), [Php](https://github.com/starlangsoftware/NER-Php), or [C#](https://github.com/starlangsoftware/NER-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-NER

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Corpus will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/NER-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `NER-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

## ParseTree

In order to find the named entities in a parse tree, one uses autoNER method of the TreeAutoNER class.

	parseTree = ...
	turkishNer = TurkishTreeAutoNER(ViewLayerType.Turkish)
	turkishNer.autoNER(parseTree)

## Sentence

In order to find the named entities in a simple sentence, one uses autoNER method of the SentenceAutoNER class.

	sentence = ...
	turkishNer = TurkishSentenceAutoNER()
	turkishNer.autoNER(sentence)

# Cite

	@INPROCEEDINGS{8093439,
  	author={B. {Ertopçu} and A. B. {Kanburoğlu} and O. {Topsakal} and O. {Açıkgöz} and A. T. {Gürkan} and B. {Özenç} and İ. {Çam} and B. {Avar} and G. {Ercan} 	and O. T. {Yıldız}},
  	booktitle={2017 International Conference on Computer Science and Engineering (UBMK)}, 
  	title={A new approach for named entity recognition}, 
  	year={2017},
  	volume={},
  	number={},
  	pages={474-479},
  	doi={10.1109/UBMK.2017.8093439}}

For Contibutors
============

### Setup.py file
1. Do not forget to set package list. All subfolders should be added to the package list.
```
    packages=['Classification', 'Classification.Model', 'Classification.Model.DecisionTree',
              'Classification.Model.Ensemble', 'Classification.Model.NeuralNetwork',
              'Classification.Model.NonParametric', 'Classification.Model.Parametric',
              'Classification.Filter', 'Classification.DataSet', 'Classification.Instance', 'Classification.Attribute',
              'Classification.Parameter', 'Classification.Experiment',
              'Classification.Performance', 'Classification.InstanceList', 'Classification.DistanceMetric',
              'Classification.StatisticalTest', 'Classification.FeatureSelection'],
```
2. Package name should be lowercase and only may include _ character.
```
    name='nlptoolkit_math',
```

### Python files
1. Do not forget to comment each function.
```
    def __broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Determines the broadcasted shape of two tensors.

        :param shape1: Tuple representing the first tensor shape.
        :param shape2: Tuple representing the second tensor shape.
        :return: Tuple representing the broadcasted shape.
        """
```
2. Function names should follow caml case.
```
    def addItem(self, item: str):
```
3. Local variables should follow snake case.
```
	det = 1.0
	copy_of_matrix = copy.deepcopy(self)
```
4. Class variables should be declared in each file.
```
class Eigenvector(Vector):
    eigenvalue: float
```
5. Variable types should be defined for function parameters and class variables.
```
    def getIndex(self, item: str) -> int:
```
6. For abstract methods, use ABC package and declare them with @abstractmethod.
```
    @abstractmethod
    def train(self, train_set: list[Tensor]):
        pass
```
7. For private methods, use __ as prefix in their names.
```
    def __infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
```
8. For private class variables, use __ as prefix in their names.
```
class Matrix(object):
    __row: int
    __col: int
    __values: list[list[float]]
```
9. Write \_\_repr\_\_ class methods as toString methods
10. Write getter and setter class methods.
```
    def getOptimizer(self) -> Optimizer:
        return self.optimizer
    def setValue(self, value: Optional[Tensor]) -> None:
        self._value = value
```
11. If there are multiple constructors for a class, define them as constructor1, constructor2, ..., then from the original constructor call these methods.
```
    def constructor1(self):
        self.__values = []
        self.__size = 0

    def constructor2(self, values: list):
        self.__values = values.copy()
        self.__size = len(values)

    def __init__(self,
                 valuesOrSize=None,
                 initial=None):
        if valuesOrSize is None:
            self.constructor1()
        elif isinstance(valuesOrSize, list):
            self.constructor2(valuesOrSize)
```
12. Extend test classes from unittest and use separate unit test methods.
```
class TensorTest(unittest.TestCase):

    def test_inferred_shape(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual((2, 2), a.getShape())

    def test_shape(self):
        a = Tensor([1.0, 2.0, 3.0])
        self.assertEqual((3, ), a.getShape())
```
13. Enumerated types should be used when necessary as enum classes.
```
class AttributeType(Enum):
    """
    Continuous Attribute
    """
    CONTINUOUS = auto()
    """
    Discrete Attribute
    """
    DISCRETE = auto()
```
