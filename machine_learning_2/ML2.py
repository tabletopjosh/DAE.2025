# Full Python code covering all 5 criteria

# Install required packages if not already installed
# pip install scikit-learn matplotlib gym

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, silhouette_score
import gym

# 1. Decision Trees and Random Forests
print("=== Decision Trees vs Random Forests ===")
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)

tree_accuracy = accuracy_score(y_test, y_pred_tree)

forest_model = RandomForestClassifier(random_state=42)
forest_model.fit(X_train, y_train)
y_pred_forest = forest_model.predict(X_test)

forest_accuracy = accuracy_score(y_test, y_pred_forest)

print(f"Decision Tree Accuracy: {tree_accuracy:.2f}")
print(f"Random Forest Accuracy: {forest_accuracy:.2f}")

# 2. Support Vector Machines (SVM)
print("\n=== Support Vector Machine ===")
svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)

svm_accuracy = accuracy_score(y_test, y_pred_svm)
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred_svm, average='weighted')

print(f"SVM Accuracy: {svm_accuracy:.2f}")
print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}")

# 3. Clustering Techniques
print("\n=== K-Means Clustering ===")
X_cluster = iris.data
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_cluster)
labels = kmeans.labels_

silhouette_avg = silhouette_score(X_cluster, labels)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# Visualize Clusters
plt.scatter(X_cluster[:, 0], X_cluster[:, 1], c=labels, cmap='viridis')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# 4. Reinforcement Learning (Simple Q-Learning in FrozenLake)
print("\n=== Reinforcement Learning (FrozenLake) ===")
env = gym.make("FrozenLake-v1", is_slippery=False)
n_actions = env.action_space.n
n_states = env.observation_space.n

Q = np.zeros((n_states, n_actions))

episodes = 1000
learning_rate = 0.8
gamma = 0.95
rewards = []

for episode in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action = np.argmax(Q[state, :] + np.random.randn(1, n_actions) * (1.0 / (episode + 1)))
        new_state, reward, done, _, _ = env.step(action)
        Q[state, action] = Q[state, action] + learning_rate * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        total_reward += reward
        state = new_state
    rewards.append(total_reward)

# Plot rewards over episodes
plt.plot(range(episodes), np.cumsum(rewards))
plt.title("Cumulative Rewards Over Time")
plt.xlabel("Episodes")
plt.ylabel("Cumulative Reward")
plt.show()

# 5. Comparative Model Evaluation (Tree vs SVM)
print("\n=== Comparative Model Evaluation ===")
print(f"Decision Tree Accuracy: {tree_accuracy:.2f}")
print(f"Random Forest Accuracy: {forest_accuracy:.2f}")
print(f"SVM Accuracy: {svm_accuracy:.2f}")

# Summary Plot
models = ['Decision Tree', 'Random Forest', 'SVM']
accuracies = [tree_accuracy, forest_accuracy, svm_accuracy]

plt.bar(models, accuracies)
plt.ylim(0, 1)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

print("\nAll tasks complete!")