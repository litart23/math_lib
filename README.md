def add(a, b):
    """
    Складывает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма a и b.
    test
    import numpy as np 
    qa = np.array([[1,2,3],[4,5,6]])
    b = np.transpose(qa) #or qa.T
    np.dot(b,qa) # multiplication
    b.shape #dimetions
    print(qa)
    take_col = qa[:,:2] # taking first two column
    reshape = qa.reshape(-1,1) # creating a new columns
    reshape
    """
    return a + b

def subtract(a, b):
    """
    Вычитает второе число из первого.

    :param a: Первое число.
    :param b: Второе число.
    :return: Разность a и b.
    """
    return a - b

def multiply(a, b):
    """
    Умножает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Произведение a и b.
    """
    return a * b

def divide(a, b):
    """
    Делит первое число на второе.

    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления a на b.
    :raises ZeroDivisionError: Если b равно 0.
    """
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль!")
    return a / b


def numpym(a, b):
    """
    import numpy as np 
    qa = np.array([[1,2,3],[4,5,6]])
    b = np.transpose(qa) #or qa.T
    np.dot(b,qa) # multiplication
    b.shape #dimetions
    print(qa)
    take_col = qa[:,:2] # taking first two column
    reshape = qa.reshape(-1,1) # creating a new columns
    reshape
    """
    return a + b


def helpm(a, b):
    """
    all imports:
    one_m - basic 
    two_m - Кластеризация, к-means, ++, inertia, elbow, silhoette, convex, hierarchical, euclidian distance
    three_m - single complete and centroid linkage, agglomerative and divisive clustering
    four_m - sklearn, fit, predict, transform
    five_m - soft clustering, fuzzy, c-means, generalized inertia, eigenvectors, eigenvalues
    six_m - svd, norm, rank, threshold, pca, projections!
    seven_m - ICA
    eight_m - Anomaly detection, dbscan, iso forest, iso tree, hyper-parameters, NMF, components of it
    nine_m = ten_m
    ten_m - Text features, bag of words, word embedings, text preprocessing, stemming, lemmatization, tf-idf, n-gramns, topic-modeling, LDA

    Vocabulary
    Centroid: The mean of all points in a cluster.
    Linkage: The method used to determine the distance between clusters in hierarchical clustering.
    Orthonormal: Vectors that are both orthogonal (perpendicular) and normalized (length = 1).
    Orthogonal: Vectors that are perpendicular to each other (dot product = 0).
    Eigenvalues: Scalars that indicate the magnitude of the eigenvectors in PCA.
    Projection: Mapping data points onto a lower-dimensional space (e.g., PCA).
    Anomaly Score: A measure used in Isolation Forest to identify outliers.
    Non-Negative Matrix Factorization (NMF): A technique for factorizing a matrix into two non￾negative matrices.
    Topic Modeling: A technique for discovering abstract topics in a collection of documents (e.g., LDA).
    """     
    return a + b

def ten(a, b):
    """
        1. Text Features (Текстовые признаки)
        Текстовые признаки — это числовые представления текста, которые можно использовать в машинном обучении. Поскольку алгоритмы ML работают с числами, текст нужно преобразовать в числовой формат.
        2. Bag of Words (Мешок слов)
        Bag of Words (BoW) — это простой способ представления текста в виде вектора, где каждый элемент вектора соответствует частоте слова в тексте.
    Как работает?
    Создается словарь всех уникальных слов в текстах.
    Каждый текст представляется в виде вектора, где каждый элемент показывает, сколько раз слово встречается в тексте.
    Пример:
    Тексты:
    "I love cats"
    "I hate cats"
    Словарь: ['I', 'love', 'hate', 'cats']
    Векторы:
    "I love cats" → [1, 1, 0, 1]
    "I hate cats" → [1, 0, 1, 1]
    Проблемы:
    Игнорирует порядок слов.
    Не учитывает семантику (значение слов).

    3. Word Embeddings (Векторные представления слов)
    Что это?
    Word Embeddings — это способ представления слов в виде векторов в многомерном пространстве, где семантически близкие слова находятся близко друг к другу.
    Примеры моделей:
    Word2Vec.Как работает?
    Модель обучается на большом корпусе текстов.
    Каждое слово представляется в виде вектора (например, 100-мерного).
    Пример:
    Слова "king" и "queen" будут близки в векторном пространстве.
    Слова "king" и "apple" будут далеки.
    4. Text Preprocessing (Предобработка текста)
    Предобработка текста — это подготовка текста для анализа. Включает:
    Удаление стоп-слов.
    Стемминг или лемматизацию.
    Приведение к нижнему регистру.
    Удаление пунктуации и специальных символов.
    5. Stopwords (Стоп-слова)
    Что это?
    Стоп-слова — это слова, которые не несут смысловой нагрузки (например, "и", "в", "на").
    Зачем удалять?
    Уменьшают размер данных.
    Улучшают качество анализа.
    Пример:
    Исходный текст: "Я иду в магазин"
    После удаления стоп-слов: "иду магазин"
    6. Stemming (Стемминг)
    Что это?
    Стемминг — это процесс приведения слова к его корневой форме.
    Пример:
    Слова "running", "runner", "runs" → "run"
    7. Lemmatization (Лемматизация)
    Что это?
    Лемматизация — это процесс приведения слова к его словарной форме (лемме).
    Пример:
    Слова "running", "runner", "runs" → "run"
    8. TF-IDF (Term Frequency-Inverse Document Frequency)
    Что это?
    TF-IDF — это статистическая мера, которая оценивает важность слова в документе относительно коллекции документов.
    Как работает?
    TF (Term Frequency): Частота слова в документе.
    IDF (Inverse Document Frequency): Логарифм обратной частоты документа, содержащего слово.
    Пример:
    Слово "the" встречается часто, но не важно (низкий TF-IDF).
    Слово "cat" встречается редко, но важно (высокий TF-IDF).
    Формула:
    TF-IDF(t,d)=TF(t,d)×log( DF(t)N )
    где:
    t — термин (слово).
    d — документ.
    N — общее число документов.
    DF(t) — число документов, содержащих термин t.
    9. n-Grams (n-граммы)
    Что это?
    n-Grams — это последовательности из n слов или символов.
    Пример:
    Биграммы (2-граммы): "I love", "love cats"
    Триграммы (3-граммы): "I love cats"
    Учитывает контекст и порядок слов.
    10. LDA (Latent Dirichlet Allocation)
    Что это?
    LDA — это метод тематического моделирования, который находит скрытые темы в документах. 
    Каждый документ представляется как смесь тем.
    Каждая тема — это распределение слов.
    Пример:
    Тема 1: "кошки", "собаки", "животные"
    Тема 2: "программирование", "алгоритмы", "код"
    Применение:
    Классификация документов.
    Поиск скрытых тем.
    Description: LDA is a generative probabilistic model used for topic modeling. It assumes that
    documents are mixtures of topics and topics are mixtures of words.
    Steps:
    1. Initialize topic distributions for each document.
    2. Initialize word distributions for each topic.
    3. Iteratively update the distributions using Gibbs sampling or variational inference.
    """
    return a + b

def one(a, b):
    """
    Основы, вектора и матрицы, ортогональность.
    Ортогональные векторы перпендикулярны друг другу, 
    их произведение равно нулю Ортогонормальная матрица - квадратная, если умножить её на транспонированную матрицу, то получится единичная матрица
    # Единичная матрица:
    import numpy as np
    a = np.array([[1,0],[0,1]])
    #Как транспонировать с numpy:
    #help(np.transpose)
    qa = np.array([[1,2,3],[4,5,6]])
    b = np.transpose(qa)
    qa, b
    np.dot(b,qa) # Умножение матриц
    b.shape, qa.shape #узнать размерность
    """
    return a + b

def two(a, b):
    """
    Глава 2. Кластеризация, к-means, ++, inertia, elbow, silhoette, convex, hierarchical, euclidian distance
    Метод Elbow (локтя)
    Используется для выбора оптимального количества кластеров в K-Means.
    Суть:
    Вычисляем сумму квадратов расстояний от точек до их центроида (Within-Cluster Sum of Squares, WCSS).
    Строим график зависимости WCSS от числа кластеров k.
    Ищем "локоть" — точку, где прирост качества значительно замедляется

    Инерция — это сумма квадратов расстояний всех точек до их ближайшего центроида.
    Чем меньше инерция, тем лучше кластеризация (но слишком малое значение может означать переобучение).
    ИНерция(Inertia) - это внутрикластерное квадратичное расстояние!
    крч, берём первый кластер и считаем сумму квадратов расстояния всех точек до центроиды
    затем так считаем для n кластеров, их может быть 5, 10 и тд и для каждого кластера рассчитываем 

    elbow:
    # Генерируем случайные данные
    X = np.random.rand(100, 2)

    # Считаем WCSS для разных k
    wcss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)  # inertia_ = сумма квадратов расстояний до центроидов

    # Рисуем график
    plt.plot(range(1, 11), wcss, marker='o')
    plt.xlabel("Количество кластеров (k)")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.show()

    from sklearn.metrics import silhouette_score
    # Запускаем KMeans с 3 кластерами
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    # Считаем силуэт
    sil_score = silhouette_score(X, labels)
    print(f"Silhouette Score: {sil_score:.3f}")

    В принципе думаю стоит начать с дистанции эвклида, благо это прошёл и это часть одна из самых доступных И так, чтобы найти дистацию между 
    координатами векторов допустим [a1,a2] и [b1,b2] нам нужно dist = math.sqrt((([a1-b1])**2+([a2-b2])**2) крч найти разницу между первыми 
    значениями векторов, вывозвести в квадрат, сложить с разницей вторых значений из первого и второго вектора, 
    тоже в квадрат, и тд, пока не дойдём до последнего значения, а потом всю эту сумму взять в корень. Вот отличный самописный пример:

    import numpy as np
    import math
    a,b,c,d = [1, 2, 3], [0, 3, 3], [4, 2, 9], [2, 2, 2]
    def euc(first):    
        origin = [0,0,0]
        len_first = len(first) # check size of vectors
        len_origin = len(origin) 
        if len_first > len_origin:
            for i in range(len_first - len_origin):
                origin = origin+[0]
        #print(origin)
        if len_first < len_origin:
            for i in range(len_origin - len_first ):
                first = first+[0]
        #print(first)
        sum = 0
        for i in range(len_first):
            sum = sum + (first[i]-origin[i])**2
        final_sum = math.sqrt(sum)     
        #print(final_sum)
        return(final_sum)

    vectors = a,b,c,d
    def find(vectors):
        dist=[]
        for vector in range(len(vectors)):
            dist = dist + [euc(vectors[vector])]
        min_dist = min(dist)  
        min_arg = dist.index(min_dist)
        print(f"{vectors[min_arg]} - the closest vector, the distance is {min_dist}")
        print()
    find(vectors)  


    тут по сути первая функция - это проверка на длины векторов, а зачем нахождение дистанции между 
    первым и вторым вектором. Вторая же функция берёт все вектора, находит для каждого дистанцию, а затем с помощью функции min() находит минимальное значение
    есть ещё полезная функция из numpy, для нахождение дистанции в одну строчку:

    first, origin = np.array([1, 2, 3]), np.array([0, 3, 3])
    sum = np.linalg.norm(first - origin, axis = 0) # линалг.норм, но перед этим нужно конвертнуть вектора в np.array
    sum

    Как устроен К-mean, алгоритм:
    Выбираем кол-во кластеров
    Выбираем центроиды
    Считаем расстояния до центроид и для каждой точки определяем к какой центроиде та или иная принадлежит
    После определения каждой точки к центроиде высчитываем среди этих точек новую центроиду (складывая все по оси х, а затем деля на кол-во точек, затем также для y и по остальным осям, в итоге получаем новую координаты для центроида)
    повторяем 3-4 пока или не кончатся итерации заданные либо пока центроиды не перестали двигаться

    K++: 
    Выбираем первый центроид случайно из всех точек.
    Для каждой точки  находим минимальное расстояние до ближайшего центроида:
    Считаем вероятность выбора точки по формуле с евклидовой дистанцией
    ем дальше точка от ближайшего центроида, тем выше её вероятность быть следующим центроидом.
    Выбираем следующий центроид случайно, но с учётом вероятностей 
    Повторяем шаги 2-4, пока не выбрано k центроидов.

    from sklearn.cluster import KMeans
    #KMeans(    n_clusters=8,    *,    init='k-means++',    n_init='auto',    max_iter=300,     random_state=None,    copy_x=True,    algorithm='lloyd',)
    import numpy as np
    X = np.random.uniform(0, 10, (100, 2))
    kmeans = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(X)
    kmeans.labels_
    kmeans.predict([[0, 0], [12, 3]])
    kmeans.cluster_centers_
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.title("кластеризация")
    plt.show()

    Алгоритм агломеративной (hierarchical) кластеризации
    Начало: каждая точка — это свой кластер.
    Объединение: находим ближайшие кластеры и объединяем их.
    Повторяем до тех пор, пока не останется нужное количество кластеров.
    Результат: создаётся дендрограмма (дерево кластеров).
    Методы измерения "близости" кластеров (linkage):
    Single linkage — минимальное расстояние между точками разных кластеров.
    Complete linkage — максимальное расстояние между точками.
    Average linkage — среднее расстояние между всеми точками.
    Ward linkage — минимизирует увеличение дисперсии внутри кластеров.

    Ключевые параметры в AgglomerativeClustering (sklearn)
    n_clusters — сколько кластеров оставить.
    linkage — метод объединения ('ward', 'single', 'complete', 'average').
    affinity — метрика расстояния (обычно 'euclidean').

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.cluster import AgglomerativeClustering
    from scipy.cluster.hierarchy import dendrogram, linkage
    # Генерируем случайные данные
    X = np.array([[1, 2], [2, 3], [3, 4], [8, 7], [8, 8], [9, 7]])
    # Запускаем агломеративную кластеризацию (2 кластера, метод Ward)
    clustering = AgglomerativeClustering(n_clusters=2, linkage='ward')
    labels = clustering.fit_predict(X)
    # Визуализация результатов кластеризации
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
    plt.title("Agglomerative Clustering")
    plt.show()
    # Строим дендрограмму
    linked = linkage(X, method='ward')
    plt.figure(figsize=(8, 5))
    dendrogram(linked, labels=range(len(X)))
    plt.title("Dendrogram")
    plt.show()

    как найти собственные вектора и значения
    test = np.array([[1, 2, 3], [0, 3, 3], [4, 2, 9]])
    eigenvalues, eug = np.linalg.eig(test)
    eigenvalues, eug
    """
    return a + b

def three(a, b):
    """
    И так, линкаджи - это методы рассчёта расстояния между кластерами
    Agglomerative: снизу вверх, объединяет кластеры. Чаще используется. Divisive: сверху вниз, разделяет кластеры. Редко применяется из-за сложности.
    """
    return a + b

def four(a, b):
    """
    sklearn, fit, predict, transform

    fit: Обучает модель на данных.
    predict: Делает предсказания на новых данных.
    transform: Преобразует данные (например, снижает размерность).
    Задача: Уменьшить количество признаков в данных.
    Шаги: Создаем данные.
    Обучаем модель PCA.
    Преобразуем данные.
    kmeans:
    Создаем данные. Обучаем модель K-means. Делаем предсказания.

    from sklearn.cluster import KMeans
    import numpy as np
    import matplotlib.pyplot as plt
    # 1. Создаем данные
    X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    # 2. Обучаем модель K-means
    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(X)  # fit — обучаем модель
    # 3. Делаем предсказания
    labels = kmeans.predict(X)  # predict — предсказываем кластеры
    print("Метки кластеров:", labels)
    # Визуализация
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')  # Центроиды
    plt.title("K-means кластеризация")
    plt.show()

    или ПСА

    from sklearn.decomposition import PCA
    import numpy as np
    import matplotlib.pyplot as plt
    # 1. Создаем данные
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    # 2. Обучаем модель PCA
    pca = PCA(n_components=1)
    pca.fit(X)  # fit — обучаем модель
    # 3. Преобразуем данные
    X_transformed = pca.transform(X)  # transform — преобразуем данные
    print("Преобразованные данные:\n", X_transformed)
    # Визуализация
    plt.scatter(X[:, 0], X[:, 1], label='Исходные данные')
    plt.scatter(X_transformed, [0] * len(X_transformed), label='Преобразованные данные')
    plt.legend()
    plt.title("PCA")
    plt.show()

    """
    return a + b

def five(a, b):
    """
     soft clustering, fuzzy, c-means, generalized inertia, eigenvectors, eigenvalues

    NMF: В Non-Negative Matrix Factorization (NMF), W H — это матрицы, на которые разлагается исходная матрица V, причем все элементы 
    этих матриц неотрицательны. Разложение помогает выделить скрытые (латентные) структуры данных, что особенно полезно в таких задачах, 
    как тематическое моделирование или извлечение признаков. W представляет собой "темы" или "латентные компоненты". В контексте текста, 
    например, это может быть матрица, где каждая строка W представляет скрытую тему (или скрытую характеристику), а каждый столбец — вес,
    с которым эта тема участвует в различных объектах (документах). Каждая строка W соответствует тому, как каждая тема представлена
    в исходных данных. Матрица H (размерность 𝑟×𝑛): H представляет собой активацию компонент или весовые коэффициенты для объектов 
    (например, документов). В контексте текста это матрица, где каждая строка H соответствует весу темы для каждого объекта

    Eigenvectors показывают особые направления, в которых матрица просто масштабирует вектор, а Eigenvalues говорят, насколько сильно.

    Fuzzy C-Means — это метод кластеризации, похожий на K-Means, но вместо чёткого деления
    точек на кластеры он позволяет каждой точке принадлежать сразу к нескольким кластерам с разной степенью уверенности. Алгоритм Fuzzy C-Means (словами)
    1.Задаём число кластеров k и случайно инициализируем их центры.
    2.Рассчитываем, насколько каждая точка принадлежит каждому кластеру. Используем степень принадлежности (membership): чем ближе точка к центру кластера, тем сильнее она к нему относится.
    3.Обновляем центры кластеров: Новые центры считаются как взвешенное среднее всех точек, с учётом их степени принадлежности.
    4.Повторяем шаги 2–3, пока центры не стабилизируются или изменения становятся минимальными.     

    import numpy as np
    import skfuzzy as fuzz
    import matplotlib.pyplot as plt
    # Генерируем случайные точки
    X = np.random.rand(100, 2)
    # Применяем Fuzzy C-Means с 2 кластерами
    cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(X.T, c=2, m=2, error=0.005, maxiter=1000)
    # Определяем принадлежность точек кластерам
    max_membership = np.max(u, axis=0)  # Находим степень уверенности для каждой точки
    cluster_labels = np.argmax(u, axis=0)  # Основной кластер для каждой точки
    # Определяем "неопределённые" точки (если max_membership < 0.6)
    uncertain_points = max_membership < 0.6
    # Визуализация
    plt.scatter(X[~uncertain_points, 0], X[~uncertain_points, 1], c=cluster_labels[~uncertain_points], cmap='coolwarm', alpha=0.7, label="Чёткие точки")
    plt.scatter(X[uncertain_points, 0], X[uncertain_points, 1], c='green', marker='o', edgecolors='black', label="Спорные точки")  # Спорные точки
    plt.scatter(cntr[:, 0], cntr[:, 1], c='black', marker='x', s=200, label="Центры кластеров")
    plt.legend()
    plt.show()

    """
    return a + b

def six(a, b):
    """
    до SVD и обратно
    import numpy as np
    # Матрица A (3x2)
    A = np.array([
        [3, 2],
        [2, 3],
        [1, 0]
    ])
    # SVD разложение
    U, Sigma, Vt = np.linalg.svd(A)
    print("U:\n", U)
    print("Sigma:\n", Sigma)  # Выводит 1D массив значений σ
    print("V^T:\n", Vt)
    s_matrix = np.zeros((3,2))
    for i in range(Sigma.size):
        s_matrix[i,i]=Sigma[i]
    #
    t = U@s_matrix@Vt
    s_matrix,t.round()

    PCA:
    Description: A dimensionality reduction technique that projects data onto orthogonal axes (principal
    components) that capture the most variance.
    Steps:
    1. Compute the mean of the data.
    2. Subtract the mean from each observation.
    3. Compute the covariance matrix.
    4. Perform eigenvalue decomposition on the covariance matrix.
    5. Select the top k eigenvectors (principal components).

    from sklearn.decomposition import PCA
    import numpy as np
    import matplotlib.pyplot as plt
    # 1. Создаем данные
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    # 2. Обучаем модель PCA
    pca = PCA(n_components=1)
    pca.fit(X)  # fit — обучаем модель
    # 3. Преобразуем данные
    X_transformed = pca.transform(X)  # transform — преобразуем данные
    print("Преобразованные данные:\n", X_transformed)
    # Визуализация
    plt.scatter(X[:, 0], X[:, 1], label='Исходные данные')
    plt.scatter(X_transformed, [0] * len(X_transformed), label='Преобразованные данные')
    plt.legend()
    plt.title("PCA")
    plt.show()

    Projection b on two main components U:
    U = np.array([[2,0,-2,0],[0,1,0,0],[2,0,2,0],[0,0,0,1]])
    U2 = U [:,:2]
    b = np.array([4,3,2,1]).reshape(-1,1)
    U2@U2.T@b
    """
    return a + b

def seven(a, b):
    """
    Что делает ICA?
    ICA помогает извлекать независимые компоненты из многомерных данных. 
    Например, в задаче с источниками звука (слушаемая музыка, речь и т.д.), 
    ICA может помочь разделить смесь этих звуков в независимые источники (если они не слишком сильно перекрываются).
    Что происходит в fit_transform?
    Когда ты вызываешь метод fit_transform, ты обучаешь модель ICA на данных, а затем сразу преобразуешь эти данные 
    в новое пространство, в котором данные представлены в виде независимых компонент.

    ICM steps: 
    Как работает ICA простыми словами
    1) Делаем данные удобными — вычитаем среднее, чтобы центрировать их вокруг нуля.
    2) Убираем корреляции — делаем так, чтобы данные не зависели друг от друга (сжимаем их в сферическую форму, как в PCA).
    3) Ищем скрытые источники — пытаемся найти такие направления, где сигналы становятся максимально разными и независимыми.
    4) Разделяем их — теперь у нас есть набор независимых компонентов, которые были смешаны в данных (например, можно разделить 
    звуки разных людей, говорящих одновременно). 

    from sklearn.decomposition import FastICA

    ica = FastICA(n_components = 2)
    S = ica.fit_transform(X)
    S

    # Создаём искусственные данные (смесь двух независимых источников)
    # Источник 1 и Источник 2
    S1 = np.sin(2 * np.pi * 0.1 * np.arange(2000))
    S2 = np.sign(np.sin(2 * np.pi * 0.05 * np.arange(2000)))

    # Смешиваем источники
    S = np.c_[S1, S2]
    A = np.array([[1, 1], [0.5, 2]])  # Матрица смешивания
    X = S.dot(A.T)  # Полученная смесь
    # Применяем ICA для извлечения независимых компонент
    ica = FastICA(n_components=2)
    S_ = ica.fit_transform(X)  # В S_ мы получаем независимые компоненты
    print(S1)
    print(S_)  # (2000, 2), 2 независимых компонента
    """

    return a + b

def eight(a, b):
    """
    Anomaly detection, dbscan, iso forest, iso tree, hyper-parameters, NMF, components of it
    DBSCAN - два главных параметра, 1)радиус поиска и 2) минимальное число точек чтобы сформировать кластер
    Что такое Isolation Forest? Isolation Forest — это алгоритм машинного обучения, который используется для обнаружения аномалий. 
    Он основан на идее, что аномалии — это редкие и отличающиеся точки данных, которые можно "изолировать" (отделить) быстрее, чем нормальные данные.

    #Isolation forest:
    from sklearn.ensemble import IsolationForest
    import numpy as np
    import matplotlib.pyplot as plt
    # Создаем данные
    X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0], [5, 3]])
    # Применяем Isolation Forest
    iso_forest = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    iso_forest.fit(X)
    # Предсказание аномалий
    predictions = iso_forest.predict(X)
    print("Предсказания (1 = нормальная точка, -1 = аномалия):", predictions)
    # Визуализация
    plt.scatter(X[:, 0], X[:, 1], c=predictions, cmap='viridis')
    plt.title("Isolation Forest")
    plt.show()
    #Объяснение:
    #Мы создали данные с двумя признаками.
    #Isolation Forest пометил аномалии (точки, которые далеки от основной массы данных).
    #На графике аномалии выделены другим цветом.

    NMF - algorithm:
    1) initialize W 2) compute H using least squares (projection) and replace any negative values with 0 
        3) compute W using lest... 4) repeat steps 2 and 3 until convergence
    two hyper-parameters: 1)n_components(number of columns in W and number of rows in H)
    2) randome state(seed)

    NMF: В Non-Negative Matrix Factorization (NMF), 
    W H — это матрицы, на которые разлагается исходная матрица V, причем все элементы этих матриц неотрицательны. 
    Разложение помогает выделить скрытые (латентные) структуры данных, что особенно полезно в таких задачах,
    как тематическое моделирование или извлечение признаков.
    W представляет собой "темы" или "латентные компоненты".
    В контексте текста, например, это может быть матрица, где каждая строка 
    W представляет скрытую тему (или скрытую характеристику), а каждый столбец — вес, 
    с которым эта тема участвует в различных объектах (документах).
    Каждая строка W соответствует тому, как каждая тема представлена в исходных данных.
    Матрица H (размерность 𝑟×𝑛):
    H представляет собой активацию компонент или весовые коэффициенты для объектов (например, документов).
    В контексте текста это матрица, где каждая строка H соответствует весу темы для каждого объекта 

    X (m × n) — исходная матрица (например, данные о пользователях и товарах).
    𝑊
    W (m × k) — матрица "факторов" (описывает, как объекты связаны с факторами).
    𝐻
    H (k × n) — матрица "тем" (описывает, как факторы связаны с признаками).
    Что они означают?
    W (матрица объектов и факторов)

    Строки соответствуют объектам (например, пользователям).
    Столбцы — скрытые факторы (например, жанры фильмов).
    Показывает, насколько объект принадлежит каждому фактору.
    2) H (матрица факторов и признаков)

    Строки соответствуют скрытым факторам.
    Столбцы — признакам (например, конкретным фильмам).
    Показывает, насколько каждый признак относится к фактору.

    from sklearn.decomposition import NMF
    nmf = NMF(n_components=2)
    W = nmf.fit_transform(X)
    H = nmf.components_
    """
    return a + b

def nine(a, b):
    """
    1. Text Features (Текстовые признаки)
    Текстовые признаки — это числовые представления текста, которые можно использовать в машинном обучении. 
    Поскольку алгоритмы ML работают с числами, текст нужно преобразовать в числовой формат.
    2. Bag of Words (Мешок слов)
    Bag of Words (BoW) — это простой способ представления текста в виде вектора, где каждый элемент вектора соответствует частоте слова в тексте.
    Как работает?
    Создается словарь всех уникальных слов в текстах.
    Каждый текст представляется в виде вектора, где каждый элемент показывает, сколько раз слово встречается в тексте.
    Пример:
    Тексты:
    "I love cats"
    "I hate cats"
    Словарь: ['I', 'love', 'hate', 'cats']
    Векторы:
    "I love cats" → [1, 1, 0, 1]
    "I hate cats" → [1, 0, 1, 1]
    Проблемы:
    Игнорирует порядок слов.
    Не учитывает семантику (значение слов).

    3. Word Embeddings (Векторные представления слов)
    Что это?
    Word Embeddings — это способ представления слов в виде векторов в многомерном пространстве, где семантически близкие слова находятся близко друг к другу.
    Примеры моделей:
    Word2Vec.Как работает?
    Модель обучается на большом корпусе текстов.
    Каждое слово представляется в виде вектора (например, 100-мерного).
    Пример:
    Слова "king" и "queen" будут близки в векторном пространстве.
    Слова "king" и "apple" будут далеки.
    4. Text Preprocessing (Предобработка текста)
    Предобработка текста — это подготовка текста для анализа. Включает:
    Удаление стоп-слов.
    Стемминг или лемматизацию.
    Приведение к нижнему регистру.
    Удаление пунктуации и специальных символов.
    5. Stopwords (Стоп-слова)
    Что это?
    Стоп-слова — это слова, которые не несут смысловой нагрузки (например, "и", "в", "на").
    Зачем удалять?
    Уменьшают размер данных.
    Улучшают качество анализа.
    Пример:
    Исходный текст: "Я иду в магазин"
    После удаления стоп-слов: "иду магазин"
    6. Stemming (Стемминг)
    Что это?
    Стемминг — это процесс приведения слова к его корневой форме.
    Пример:
    Слова "running", "runner", "runs" → "run"
    7. Lemmatization (Лемматизация)
    Что это?
    Лемматизация — это процесс приведения слова к его словарной форме (лемме).
    Пример:
    Слова "running", "runner", "runs" → "run"
    8. TF-IDF (Term Frequency-Inverse Document Frequency)
    Что это?
    TF-IDF — это статистическая мера, которая оценивает важность слова в документе относительно коллекции документов.
    Как работает?
    TF (Term Frequency): Частота слова в документе.
    IDF (Inverse Document Frequency): Логарифм обратной частоты документа, содержащего слово.
    Пример:
    Слово "the" встречается часто, но не важно (низкий TF-IDF).
    Слово "cat" встречается редко, но важно (высокий TF-IDF).
    Формула:
    TF-IDF(t,d)=TF(t,d)×log( DF(t)N )
    где:
    t — термин (слово).
    d — документ.
    N — общее число документов.
    DF(t) — число документов, содержащих термин t.
    9. n-Grams (n-граммы)
    Что это?
    n-Grams — это последовательности из n слов или символов.
    Пример:
    Биграммы (2-граммы): "I love", "love cats"
    Триграммы (3-граммы): "I love cats"
    Учитывает контекст и порядок слов.
    10. LDA (Latent Dirichlet Allocation)
    Что это?
    LDA — это метод тематического моделирования, который находит скрытые темы в документах. 
    Каждый документ представляется как смесь тем.
    Каждая тема — это распределение слов.
    Пример:
    Тема 1: "кошки", "собаки", "животные"
    Тема 2: "программирование", "алгоритмы", "код"
    Применение:
    Классификация документов.
    Поиск скрытых тем.
    Description: LDA is a generative probabilistic model used for topic modeling. It assumes that
    documents are mixtures of topics and topics are mixtures of words.
    Steps:
    1. Initialize topic distributions for each document.
    2. Initialize word distributions for each topic.
    3. Iteratively update the distributions using Gibbs sampling or variational inference.
    """
    return a + b

