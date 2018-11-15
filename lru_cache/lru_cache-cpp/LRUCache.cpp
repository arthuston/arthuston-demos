#include "LRUCache.hpp"

LRUCache::LRUCache<K, V>(int max_size) :
        max_size(max_size) {
}

void LRUCache<K, V>::set(const K& key, const V& value) {
    data_map_t::const_iterator data_itr = data_map.find(key);
    if (data_itr != data_map.cbegin()) {
        // existing item
        data_itr->value = value;
        // move item to back (lru)
        lu_list.erase(data_itr->lu_itr);
        data_itr->lu_itr = lu_list.push_back(key);
    } else {
        if (data_map.size() == cache_size) {
            // cache full
            data_map.erase(lu_list.front());
            lu_list.pop_front();
        }
        data_map.put(key, DataItem(value, lu_list.push_back(key)));
    }
}

const V* LRUCache<K, V>::get(const K& key) {
    data_map_t::const_iterator data_itr = data_map.find(key);
    if (data_itr != data_map.cbegin()) {
        DataItem &item = *data_itr;
        lu_list.erase(item.lu_itr);
        data_list_t::iterator lu_itr = lu_list.push_back(key);
        item.last_used = lu_itr;
        return &item.value;
    }
}








    /**
     * Set value in cache.
     * @param key key
     * @param value value
     */
    void set(const K& key, const V& value);

    /**
     * Get value in cache.
     * @return value in cache or null.
     */
    const V* get(const K& key);

private:
    // data item with value and last used iterator
    class DataItem {
        DataItem(const V &value, std::list::iterator<K> &last_used) :
                value(value),
                last_used(last_used) {
            // empty
        }

        const V &getValue() {
            return value;
        }

        const std::list::iterator<K> &getLastUsed() {
            return last_used;
        }

        V value;
        std::list::iterator<K> last_used;
    }

    // last recently used list
    typedef std::list<K>

    lu_list_t;
    lu_list_t lu_list;

    typedef std::map<K, DataItem> data_map_t;
    data_map_t data_map;

}
#endif // LRU_CACHE_HPP
