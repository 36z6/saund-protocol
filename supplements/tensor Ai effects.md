

Категория Эффект / Метод Что делает Где применять
Нейросетевые и AI Tensor morphing / латентный морфинг Представляет звук как многомерный тензор и плавно интерполирует между звуками, тембрами, стилями Нейросетевой звуковой дизайн, переходы, AI-музыка
 Neural style transfer Переносит «стиль» одного аудио на «содержание» другого Ремиксы, стилизация
 Timbre transfer Меняет тембр инструмента, сохраняя исполнение Гитара → скрипка, голос → синт
 Voice conversion (RVC, So-VITS) Заменяет голос на другой Вокал, пародии, коррекция
 DDSP (Differentiable DSP) Нейросеть управляет классическими DSP-параметрами Гибридный синтез, морфинг
 Neural synthesis (RAVE, NSynth, WaveNet) Генерирует звук нейросетью Новые тембры, live
 Neural reverb / amp modeling Имитирует реверб или усилитель нейросетью Гитара, вокал, мастеринг
 Source separation as FX Разделяет трек на стемы и пересобирает Акапелла, ремикс, морфинг
 AI mastering / mixing Автоматически сводит и мастерит Быстрый релиз
 Diffusion audio (AudioLDM, Stable Audio) Генерирует или преобразует звук по тексту/аудио Саунд-дизайн
 Text-to-audio Создаёт звук по описанию Кино, игры, IDM
 Audio inpainting / outpainting Дорисовывает или продлевает аудио Реставрация, лупы
 Neural vocoder Синтезирует речь/звук из спектра Вокал, эффекты
 Embedding arithmetic «Король − мужчина + женщина = королева», но для звуков Креатив, морфинг
Тензорные и многомерные Tensor decomposition (CP/PARAFAC, Tucker) Раскладывает многомерный аудио-тензор на компоненты Разделение источников, сжатие
 Tensor Train / Tensor Ring Компактное представление тензоров Нейросети, сжатие
 Tensor networks (MPS, PEPS, MERA) Квантово-подобные тензорные сети Спекулятивный AI-аудио
 Higher-order SVD Многомерный аналог SVD Анализ, морфинг
 Multilinear PCA Многолинейный PCA Тембральный морфинг
 Tensor completion Восстанавливает пропущенные данные Реставрация, генерация
 Tensor factorization for source separation Разделяет источники через тензоры Стемы, ремиксы
 Spherical harmonics / Ambisonics as tensor Пространственный звук как тензор Иммерсив
 Quantum tensor networks Тензорные сети для квантовых вычислений Спекулятивно
Спектральные экстримы Phase vocoder extreme time-stretch Экстремальное растяжение времени без изменения высоты Эмбиент, дроны, глитч
 Spectral morphing Плавный переход между спектрами двух звуков Саунд-дизайн, переходы
 Cepstral morphing Морфинг в кепстральной области Тембральный морфинг
 Wavelet morphing Морфинг через вейвлет-преобразование Анализ, креатив
 Hilbert transform / analytic signal Выделяет огибающую и мгновенную фазу Модуляция, анализ
 Instantaneous frequency Мгновенная частота сигнала Анализ, эффекты
 Teager–Kaiser energy operator Оценка энергии сигнала Детекция, модуляция
 NMF, PCA, ICA Разложение на компоненты Разделение, анализ
 Harmonic/percussive separation Разделяет гармонику и перкуссию Ремиксы, морфинг
 Sinusoidal modeling Представление звука синусоидами Синтез, морфинг
 Spectral freezing Замораживает спектр Дроны, эмбиент
 Spectral delay / reverb Дилей и реверб по частотам Креатив, пространство
 Spectral gate Гейт по частотам Чистка, эффекты
 Spectral blur Размывает спектр Эмбиент, текстуры
 Spectral compressor Компрессия по полосам Мастеринг, креатив
Физическое моделирование Modal synthesis Синтез через модальные резонансы Ударные, металл, стекло
 Karplus–Strong Струнный синтез Гитара, бас, арфа
 Waveguide synthesis Волноводный синтез Духовые, струнные
 Finite element method audio Акустика через МКЭ Научные, точные модели
 Boundary element method Акустика через МГЭ Пространство, резонанс
 Acoustic holography Восстановление акустического поля Измерения, иммерсив
 Resonant filter banks Банки резонансных фильтров Форманты, креатив
 Physical modeling morphing Морфинг физических моделей Материал → материал
 Material morphing Дерево → металл → стекло Саунд-дизайн
Иммерсив и пространство Higher-order ambisonics (HOA) Многоканальное пространственное аудио VR, кино, инсталляции
 Wave field synthesis Синтез волнового поля Концертные залы, инсталляции
 HRTF personalization Персонализация передаточной функции головы Наушники, бинауральный
 Binaural rendering Бинауральный рендеринг Наушники, VR
 Dolby Atmos, DTS:X, MPEG-H Объектно-ориентированный звук Кино, музыка, стриминг
 6DoF audio Звук с шестью степенями свободы VR, игры
 Object-based audio Объектный аудио Иммерсив, интерактив
 Beamforming Формирование луча Микрофоны, колонки
 Sonic holography Звуковая голография Креатив, наука
 Ambisonic morphing Морфинг амбисоник-полей Пространственный морфинг
Гранулярные и микро-звуковые Granular synthesis Синтез из зёрен Эмбиент, текстуры, IDM
 Grain cloud Облако зёрен Атмосфера, дроны
 Particle synthesis Синтез частицами Микро-звук
 Concatenative synthesis Сборка из фрагментов Вокал, реставрация
 Microsound Работа с микро-длительностями Экспериментальная музыка
 Stochastic synthesis Стохастический синтез Шум, текстуры
 Gendy Динамический стохастический синтез Креатив, авангард
 FOF (Formant Wave Function) Формантные волновые функции Вокал, хор
 Musique concrète Конкретная музыка Коллаж, эксперимент
 Extreme time-stretch Экстремальное растяжение Дроны, эмбиент
Генеративные и алгоритмические Markov chains Цепи Маркова Генерация мелодий, ритма
 Cellular automata Клеточные автоматы Ритм, паттерны
 L-systems L-системы Структура, генерация
 Genetic algorithms Генетические алгоритмы Эволюция звука
 Swarm intelligence Роевой интеллект Параметры, генерация
 GAN, VAE, Diffusion, Transformer Генеративные нейросети AI-музыка, звук
 Reinforcement learning for mixing Обучение с подкреплением для сведения Авто-микс
 Neural cellular automata Нейроклеточные автоматы Генерация, эволюция
 Generative infilling Генеративное заполнение Дописывание, лупы
Квантовые и пост-цифровые Quantum Fourier transform Квантовое преобразование Фурье Спекулятивно
 Quantum audio processing Квантовая обработка аудио Спекулятивно
 Quantum synthesis Квантовый синтез Спекулятивно
 Quantum reverb / delay Квантовый реверб/дилей Спекулятивно
 Superposition audio Суперпозиция звука Спекулятивно
 Entanglement audio Запутанность в аудио Спекулятивно
 Qubit modulation Модуляция кубитами Спекулятивно
 Data bending Изменение данных Глитч, креатив
 Circuit bending Изменение схем Лоу-фай, шум
 Datamoshing audio Искажение данных Глитч-арт
 Glitch art Глитч-арт Эксперимент
Био/нейро/интерфейсы EEG sonification Сонификация ЭЭГ Наука, искусство
 Brain–computer interface audio Аудио через интерфейс мозг–компьютер Спекулятивно, медицина
 Neurofeedback sonification Сонификация нейрофидбека Терапия, искусство
 Biofeedback Биофидбек Перформанс, терапия
 EMG Электромиография Управление звуком
 Gesture control Жестовое управление Live, интерактив
 Haptic audio Тактильное аудио VR, доступность
 Ultrasound haptics Ультразвуковая тактильность Инсталляции, VR
Экстремальный DSP Chaos synthesis (Lorenz, Rössler) Хаотический синтез Эксперимент, шум
 Strange attractors Странные аттракторы Генерация, текстуры
 Fractal audio Фрактальное аудио Креатив, эмбиент
 Feedback loops Обратные связи Шум, дроны, экстрим
 Nonlinear dynamics Нелинейная динамика Синтез, обработка
 Infinite impulse response extreme Экстремальный IIR Фильтры, резонанс
 Wavelet morphing Вейвлет-морфинг Анализ, креатив
 Tensor morphing Тензорный морфинг AI-аудио, морфинг
 Quantum morphing Квантовый морфинг Спекулятивно
