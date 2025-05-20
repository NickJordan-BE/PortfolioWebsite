import streamlit as st

st.title("Projects")

st.write('<p>Please visit my <a href="https://www.github.com/NickJordan-BE">GitHub</a> for the code of each project.</p>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['UHealth', 'MNIST CNN in NumPy', 'Redis Server in Go', 'UMarket', 'Financial Log', 'KerasRNN'])

with tab1:
    st.title('UHealth')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[Tensorflow] :red-badge[Python] :red-badge[Pandas] :red-badge[NumPy] :red-badge[Flask]"
    )
    st.subheader('A Custom Convolutional Neural Network (CNN) for chest x-ray diagnosis.')
    st.markdown('A Full-stack application utilizing Flask, Streamlit, and Tensorflow to create a diagnosis platform' \
    ' for doctors to hold patient data and x-rays. Utilizes Keras from Tensorflow to train and deploy a CNN model for image classification ' \
    'of up to 4 labels (TB, Covid19, Pneumonia, Normal) with a 92\\% accuracy')
    st.markdown('''
                * Prototype built within 6 hours at the South Puget Sounds largest Hackathon ever with over 15 teams and
                 80 people present placing 2nd overall in the entire competition. 
                * Prototype CNN achieving 92\\% accuracy in binary classification for pneumonia patients chest x-rays.
                * Training and optimizing model further to classify 14 different abnormalities among chest x-rays with a 95% accuracy.
                * Cleaning, filtering, and augmenting 112k image dataset in batch sizes of 256 to train and test model.
                * Utilizing Google Colab hardware to train and test model.
                ''')

with tab2:
    st.title('MNIST CNN in NumPy')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[Python] :red-badge[NumPy]"
    )
    st.subheader('A custom Convolutional Neural Network using only NumPy.')
    st.markdown('This Convolutional Neural Network was built only using the NumPy library to focus on practicing low-level deep learning techniques' \
    ' such as backpropagation and forward pass functions, custom dense, convolution, maxpooling layers, and softmax activations.')
    st.markdown('''
                * Achieved 97.5% accuracy on 2,000-image subset of the MNIST dataset in just 5 training epochs.
                * Custom implementation of:
                  * Convolutional layers with stride and padding
                  * Max pooling layers
                  * Fully connected dense layers
                  * Softmax activation and categorical cross-entropy loss
                  * Forward and backward propagation
                * Trained on the MNIST dataset with minimal external dependencies
                * Modular and extensible architecture for experimentation
                * Practice multi-variable Calculus and Deep learning algorithms in low-level environment.
                * Achieved greater understanding of the Deep learning algorithms and techniques behind a CNN
                ''')

with tab3:
    st.title('Redis Server in Golang')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[Golang] :red-badge[Redis Client] :red-badge[TCP-Sockets] :red-badge[Custom RESP encoder and Decoder] :red-badge[File I/O] :red-badge[Docker] :red-badge[Kubernetes (MiniKube)]"
    )
    st.subheader('A custom Redis Server built utilizing GoRoutines and Custom Data Structures.')
    st.markdown('This project demonstrates systems-level engineering, network protocol design, and concurrent programming in Go. ' \
    'The server supports multiple concurrent client connections over TCP, interprets RESP (Redis Serialization Protocol), and emulates ' \
    'Redis-like functionality with performance and scalability in mind.')
    st.markdown('''
                * Supports over 20 core Redis commands including SET, GET, DEL, HSET, HGET, EXPIRE, and more
                * Implements Append Only File (AOF) and RDB-style snapshot backups with configurable durability settings
                * Built-in support for Redis Streams (XADD, XREAD, and basic consumer groups)
                * Key expiration system managed with goroutines and timers
                * Basic transactional support (MULTI/EXEC emulation)
                * RESP2 protocol-compliant parser and encoder
                * Thread-safe in-memory store with fine-grained locking
                * Containerized with Docker and deployable to Kubernetes via Minikube
                ''')

with tab4:
    st.title('UMarket')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[TypeScript] :red-badge[NodeJS and Express] :red-badge[ReactJS and Vite] :red-badge[PostgreSQL] :red-badge[Docker] :red-badge[Micro-Service Architecture]"
    )
    st.subheader('Social Media and Marketplace platform for UW Students.')
    st.markdown('This project was built with 2 teams, frontend and backend, with a total of 12+ members.' \
    ' My role was full-stack lead where I bounced between both teams managing bi-weekly sprints, weekly SCRUM meetings, and implementation' \
    ' on the backend and the DevOps infrastructure. I managed my leadership and developer position by leveraging other leaders’ schedules and ' \
    'creating a training pipeline to get newer team members ready to code. I also hosted presentations for example implementations and pair programming.')
    st.markdown('''
                * Directed teams of 6+ members overseeing full-stack implementation, integration, and testing.
                * Designed and implemented micro-service system architecture supporting 6 micro-services with Docker, enabling
                scalability and user growth by 200%.        
                * Implemented Backend RESTful APIs for Market and Social micro-service.
                * Created and managed bi-weekly sprints for the backend team.
                * Hosted weekly SCRUM meetings focusing on AGILE methodologies.
                * Hosted pair programming sessions with 5+ members bi-weekly.
                ''')

with tab5:
    st.title('Finance Agent Log')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[Python] :red-badge[Flask] :red-badge[ReactJS and Vite] :red-badge[LangChain] :red-badge[Firebase (NoSQL)]"
    )
    st.subheader('Finance Log and Financial Analysis Platform')
    st.markdown('This is a solo project where I developed a CRUD app for financial spending and experimented with AI Agents using' \
    ' LangChain for financial analysis of spending habits. Financial analysis highlighted good and bad spending habits with ratings in' \
    ' three categories: savings, investments, and wants, with an overall rating for the spending. It also offered ways to improve using online web-scraping data.')
    st.markdown('''
                * Utilized OpenAI API and LangChain to engineer a financial AI agent performing parallel chain processing,
                    leading to a 100% faster analysis time of transaction data.
                * Implemented financial chatbot with web-search and chat history functionality, resulting in 50% more accurate
                    responses and 25% faster response times.      
                * Built RESTful APIs with 99% success rate integrated with Firebase to provide real-time data, allowing offline
                    support and data syncing across multiple devices instantaneously.
                * Gained experience with AI Agents and NoSQL database design with CRUD operations.
                ''')

with tab6:
    st.title('RNN in Keras')
    st.write('Technologies:')
    st.markdown(
    ":red-badge[Python] :red-badge[TensorFlow] :red-badge[Pandas] :red-badge[NumPy]"
    )
    st.subheader('Recurrent Neural Network for Movie Review Analysis')
    st.markdown('This project served as my introduction to deep learning and machine learning. ' \
    'I used TensorFlow and the Keras API to build my first neural network, which analyzed the sentiment of movie reviews. ' \
    'Through this experience, I learned how to apply deep learning models to real-world problems and gained a high-level ' \
    'understanding of how recurrent neural networks (RNNs) operate. The project also gave me hands-on experience with processing ' \
    'downloaded datasets and designing model architectures.')
    st.markdown('''
                * Gained foundational experience in deep learning and machine learning concepts.
                * Built a sentiment analysis model using TensorFlow and the Keras API.
                * Developed and trained a neural network to classify movie reviews as positive or negative.
                * Learned the high-level workings of recurrent neural networks (RNNs).
                * Worked with real-world datasets and learned how to preprocess and structure input data.
                * Designed and tuned model architectures for text-based classification tasks.
                * Strengthened practical skills in applying machine learning to real-world problems.
                ''')
