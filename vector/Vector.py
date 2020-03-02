# template <typename T> class Vector { //向量模板类
# }; //Vector
# typedef int Rank; //秩
# define DEFAULT_CAPACITY  3 //默认的初始容量（实际应用中可设置为更大）
DEFAULT_CAPACITY = 3


class Vector:
    #    Rank _size; int _capacity;  T* _elem; //规模、容量、数据区
    _capacity = DEFAULT_CAPACITY
    _size = 0
    _elem = [0] * _capacity

    # protected:
    #    void copyFrom ( T const* A, Rank lo, Rank hi ); //复制数组区间A[lo, hi)
    def _copyFrom(self, A, lo, hi):
        for i in range(lo, hi):
            self._elem[i] = A[i]

    #    void expand(); //空间不足时扩容
    def _expand(self):
        if self._capacity > self._size:
            return
        else:
            self._capacity = self._capacity << 1
            oldlist = self._elem
            self._elem = [0] * self._capacity
            for i in range(len(oldlist)):
                self._elem[i] = oldlist[i]

    #    void shrink(); //装填因子过小时压缩
    def _shrink(self):
        if self._size < self._capacity >> 1:
            self._capacity = self._size << 1
            oldlist = self._elem
            self._elem = [0] * self._capacity
            for i in range(self._size):
                self._elem[i] = oldlist[i]

    #    bool bubble ( Rank lo, Rank hi ); //扫描交换
    #    void bubbleSort ( Rank lo, Rank hi ); //起泡排序算法
    def _bubblesort(self,lo,hi):
        for i in range(lo,hi):
            for j in range(lo,hi):
                if self._elem[j-1]>self._elem[j]:
                    term = self._elem[j-1]
                    self._elem[j-1] = self._elem[j]
                    self._elem[j] = term
            hi-=1
    #    Rank max ( Rank lo, Rank hi ); //选取最大元素
    #    void selectionSort ( Rank lo, Rank hi ); //选择排序算法
    #    void merge ( Rank lo, Rank mi, Rank hi ); //归并算法
    #    void mergeSort ( Rank lo, Rank hi ); //归并排序算法
    #    void heapSort ( Rank lo, Rank hi ); //堆排序（稍后结合完全堆讲解）
    #    Rank partition ( Rank lo, Rank hi ); //轴点构造算法
    #    void quickSort ( Rank lo, Rank hi ); //快速排序算法
    #    void shellSort ( Rank lo, Rank hi ); //希尔排序算法
    # // 构造函数
    # public:
    #    Vector ( int c = DEFAULT_CAPACITY, int s = 0, T v = 0 ) //容量为c、规模为s、所有元素初始为v
    #    { _elem = new T[_capacity = c]; for ( _size = 0; _size < s; _elem[_size++] = v ); } //s<=c
    #    Vector ( T const* A, Rank n ) { copyFrom ( A, 0, n ); } //数组整体复制
    #    Vector ( T const* A, Rank lo, Rank hi ) { copyFrom ( A, lo, hi ); } //区间
    #    Vector ( Vector<T> const& V ) { copyFrom ( V._elem, 0, V._size ); } //向量整体复制
    #    Vector ( Vector<T> const& V, Rank lo, Rank hi ) { copyFrom ( V._elem, lo, hi ); } //区间
    def __init__(self, capacity, size, v, A, *args):
        if capacity:
            self._capacity = capacity
            self._size = size
            self._elem = [0] * capacity
            for i in range(size):
                self._elem[i] = v
        if A:
            lo = 0
            hi = len(A)
            if len(args) > 1:
                lo = args[0]
                hi = args[1]
            self._size = (hi - lo)
            self._capacity = self._size << 1
            self._elem = [0] * self._capacity
            self._copyFrom(A, lo, hi)

    # // 析构函数
    #    ~Vector() { delete [] _elem; } //释放内部空间
    def __del__(self):
        del self._elem
        del self._size
        del self._capacity

    # // 只读访问接口
    #    Rank size() const { return _size; } //规模
    def size(self):
        return self._size

    #    bool empty() const { return !_size; } //判空
    def empty(self):
        return not self._size

    #    Rank find ( T const& e ) const { return find ( e, 0, _size ); } //无序向量整体查找
    #    Rank find ( T const& e, Rank lo, Rank hi ) const; //无序向量区间查找
    def find(self, elem, *args):
        lo = 0
        hi = self._size
        rank = -1
        if args:
            if len(args) != 2:
                raise Exception("the len of args must be 2")
            lo = args[0]
            hi = args[1]
        for i in range(lo, hi):
            if self._elem[i] == elem:
                rank = i
        return rank

    #    Rank search ( T const& e ) const //有序向量整体查找
    #    { return ( 0 >= _size ) ? -1 : search ( e, 0, _size ); }
    #    Rank search ( T const& e, Rank lo, Rank hi ) const; //有序向量区间查找
    # // 可写访问接口
    #    T& operator[] ( Rank r ); //重载下标操作符，可以类似于数组形式引用各元素
    #    const T& operator[] ( Rank r ) const; //仅限于做右值的重载版本
    def __getitem__(self, i):
        return self._elem[i]

    def __setitem__(self, i, value):
        self._elem[i] = value

    def getlist(self):
        return self._elem

    #    Vector<T> & operator= ( Vector<T> const& ); //重载赋值操作符，以便直接克隆向量
    #    T remove ( Rank r ); //删除秩为r的元素
    #    int remove ( Rank lo, Rank hi ); //删除秩在区间[lo, hi)之内的元素
    def remove(self, lo, *args):
        if lo >= self._size:
            raise Exception("lo > size")
        hi = lo + 1
        if len(args):
            hi = args[0]
        if hi == self._size:
            self._elem[lo] = 0
        while hi < self._size:
            self._elem[lo] = self._elem[hi]
            hi += 1
            lo += 1
        self._size -= hi - lo
        self._shrink()

    # Rank insert ( Rank r, T const& e ); //插入元素
    # Rank insert ( T const& e ) { return insert ( _size, e ); } //默认作为末元素插入
    def insert(self, e, *args):
        rank = self._size
        if len(args):
            rank = args[0]
        self._expand()
        i = self._size
        while i > rank:
            self[i] = self[i - 1]
            i -= 1
        self._elem[rank] = e
        self._size+=1

    #    void sort ( Rank lo, Rank hi ); //对[lo, hi)排序
    #    void sort() { sort ( 0, _size ); } //整体排序
    def sort(self,*args):
        lo =0
        hi = self._size
        if len(args):
            lo = args[0]
            hi = args[1]
        self._bubblesort(lo,hi)
    #    void unsort ( Rank lo, Rank hi ); //对[lo, hi)置乱
    #    void unsort() { unsort ( 0, _size ); } //整体置乱
    #    int deduplicate(); //无序去重
    def deduplicate(self):
        i=1
        while i<self._size:
            if self.find(self._elem[i],0,i)!=-1:
                self.remove(i)
            i+=1
    #    int uniquify(); //有序去重
    def uniquify(self):
        i=0
        j=1
        for j in range(1,self._size):
            if self._elem[i]!=self._elem[j]:
                i+=1
                self._elem[i]=self._elem[j]
        self._size = i+1
        self._shrink()

    # // 遍历
    #    void traverse ( void (* ) ( T& ) ); //遍历（使用函数指针，只读或局部性修改）
    #    template <typename VST> void traverse ( VST& ); //遍历（使用函数对象，可全局性修改）
    def traverse(self, func):
        for i in range(self._size):
            self._elem[i]=func(self._elem[i])

