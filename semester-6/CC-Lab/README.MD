**Complete Virtual Lab Guide for Exercises 1 to 8**

---

### **EXERCISE 1: Install VirtualBox & Linux Mint**

**Aim**: Install VirtualBox and set up a Linux OS (Linux Mint) in a virtual machine.

**Steps:**

1. **Download VirtualBox** from [https://www.virtualbox.org](https://www.virtualbox.org)
2. Install using default settings. No need to change options unless you know what you’re doing.
3. **Download Linux Mint ISO** from \[[https://linuxmint.com/download.php](https://linuxmint.com/download.php)]
4. Open VirtualBox, click **New**, and configure:

   * Name: `Mint22`
   * Type: Linux
   * Version: Ubuntu (64-bit)
5. Set memory size (2048 MB or more if available).
6. Create virtual hard disk:

   * VDI, Dynamically allocated, 25 GB recommended
7. Go to **Settings > Storage**, select the Empty CD icon, then choose your downloaded ISO.
8. Start VM and follow installation steps:

   * Choose "Erase disk and install Linux Mint"
   * Set timezone, keyboard layout, username, and password
   * Complete installation and restart

---

### **EXERCISE 2: Install a C Compiler and Run a Sample Program**

**Aim**: Install GCC compiler and run a sample C++ program

**Steps:**

1. Open Terminal:

```bash
sudo apt update
sudo apt install build-essential -y
```

2. Create a file:

```bash
nano welcome.cpp
```

3. Paste the following code:

```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello world" << endl;
    return 0;
}
```

4. Save and exit (Ctrl + O, Enter; Ctrl + X).
5. Compile and run:

```bash
g++ -Wall -o welcome welcome.cpp
./welcome
```

Output: `Hello world`

---

### **EXERCISE 3: Install Google App Engine and Create Hello World App**

**Aim**: Set up Google App Engine for Java using Eclipse.

**Steps:**

1. Install Java and Eclipse:

```bash
sudo apt install openjdk-11-jdk eclipse -y
```

2. Open Eclipse > Google Cloud Tools > Create New Project
3. Select App Engine Standard Java Project > Check Maven project > Fill details > Finish
4. Right-click project > Run As > App Engine
5. Open `http://localhost:8080` to see your app

---

### **EXERCISE 4: Use GAE Launcher to Launch Web Applications**

**Aim**: Deploy app from Eclipse to Google Cloud

**Steps:**

1. In Eclipse, Sign in to Google: File > Sign in to Google
2. Ensure `appengine-web.xml` is in WEB-INF
3. Right-click project > Deploy to App Engine Standard
4. Select Google account and project > Click OK

---

### **EXERCISE 5: Simulate Cloud in CloudSim and Run Scheduling Algorithm**

**Aim**: Use CloudSim to simulate cloud environment

**Steps:**

1. Download CloudSim from GitHub and import into Eclipse
2. Create a Java class with `main()` method
3. Steps in code:

   * `CloudSim.init(...)`
   * Create Datacenter
   * Create Broker
   * Create VMs
   * Create Cloudlets
   * Submit to broker
   * Start and stop simulation
4. Print results using `printCloudletList()`

---

### **EXERCISE 6: Transfer Files Between Virtual Machines**

**Aim**: Transfer files from one VM to another

**Steps:**

1. Ensure both VMs are running in VirtualBox
2. Option 1: Use Shared Folder

   * Settings > Shared Folder > Add > Auto-mount
3. Option 2: Use SCP (Secure Copy Protocol):

   * Install SSH:

```bash
sudo apt install openssh-server
```

* From source VM:

```bash
scp file.txt user@<destination_ip>:~/Downloads/
```

---

### **EXERCISE 7: Install Hadoop and Run Wordcount**

**Aim**: Set up a single-node Hadoop cluster

**Steps:**

1. Install Java:

```bash
sudo apt install openjdk-8-jdk -y
```

2. Download and extract Hadoop:

```bash
wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz
tar -xvf hadoop-2.7.3.tar.gz
```

3. Set environment variables in `.bashrc`
4. Configure `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, `yarn-site.xml`
5. Format Namenode:

```bash
hadoop namenode -format
```

6. Start services:

```bash
start-dfs.sh
start-yarn.sh
```

7. Run wordcount:

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount input output
```

---

### **EXERCISE 8: Create and Run Docker Container**

**Aim**: Install Docker and run your first container

**Steps:**

1. Install Docker:

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

2. Verify installation:

```bash
docker --version
```

3. Create Dockerfile:

```Dockerfile
FROM alpine
CMD echo "Hello, World!"
```

4. Build image:

```bash
docker build -t hello-world .
```

5. Run container:

```bash
docker run hello-world
```

Output: `Hello, World!`

---

**End of Guide**
