import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaları tanımlayan liste
points = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Mesafelerin saklanacağı liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayalım
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("En küçük Öklid mesafesi:", min_distance)
