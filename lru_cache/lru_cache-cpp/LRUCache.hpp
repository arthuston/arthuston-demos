/**
 * Least recently used cache.
 */

#ifndef LRU_CACHE_HPP
#define LRU_CACHE_HPP

#include <map>
#include <list>

template <typename K, typename V> class LRUCache {

public:

    /**
     * Constructor.
     * @param cache_size maximum cache size.
     */
     LRUCache(int max_size);

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
    typedef std::list<K> lu_list_t;
    typedef typename lu_list_t::iterator lu_itr_t;
    typedef typename lu_list_t::const_iterator const_lu_itr_t;

    // data item with value and last used iterator
    class DataItem {
        DataItem(const V &value, const const_lu_itr_t &last_used) :
                value(value),
                last_used(last_used) {
            // empty
        }

        V value;
        const_lu_itr_t last_used;
    };

    // last used list
    lu_list_t lu_list;  // last used list

    typedef std::map<K, DataItem> data_map_t;
    data_map_t data_map;

};
#endif // LRU_CACHE_HPP
