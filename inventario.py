import json
import random
from typing import Dict, List
import pickle
import os

class InventarioComplejo:
    def __init__(self, archivo_cache="inventario_cache.pkl"):
        self.archivo_cache = archivo_cache
        self.productos = self._cargar_o_generar_inventario()
        self.promociones_activas = self._generar_promociones()
        print(f"🏭 Inventario cargado: {len(self.productos)} productos")
    
    def _cargar_o_generar_inventario(self) -> Dict:
        """Carga inventario desde cache o genera uno nuevo."""
        if os.path.exists(self.archivo_cache):
            try:
                with open(self.archivo_cache, 'rb') as f:
                    productos = pickle.load(f)
                print("📦 Inventario cargado desde cache")
                return productos
            except:
                print("⚠️ Error cargando cache, generando nuevo inventario")
        
        productos = self._generar_inventario_dinamico()
        self._guardar_inventario(productos)
        return productos
    
    def _guardar_inventario(self, productos: Dict):
        """Guarda el inventario en cache."""
        try:
            with open(self.archivo_cache, 'wb') as f:
                pickle.dump(productos, f)
            print("💾 Inventario guardado en cache")
        except Exception as e:
            print(f"⚠️ Error guardando cache: {e}")
    
    def regenerar_inventario(self):
        """Fuerza la regeneración del inventario."""
        if os.path.exists(self.archivo_cache):
            os.remove(self.archivo_cache)
        self.productos = self._generar_inventario_dinamico()
        self._guardar_inventario(self.productos)
        self.promociones_activas = self._generar_promociones()
        print("🔄 Inventario regenerado completamente")
    
    def _generar_inventario_dinamico(self) -> Dict:
        """Genera un inventario realista y dinámico."""
        print("🏗️ Generando inventario dinámico...")
        
        categorias = ["electronica", "accesorios", "software", "cables", "almacenamiento", "gaming"]
        marcas = ["TechPro", "EliteGear", "PowerMax", "UltraSpeed", "ProWork", "Innovation", "DuraTech"]
        
        # Productos base con sus características
        productos_config = {
            # Electrónicos principales
            "laptop": {"precio_base": 800, "categoria": "electronica", "peso_rango": (2.0, 4.5)},
            "monitor": {"precio_base": 300, "categoria": "electronica", "peso_rango": (3.0, 8.0)},
            "tablet": {"precio_base": 400, "categoria": "electronica", "peso_rango": (0.5, 1.2)},
            "smartphone": {"precio_base": 600, "categoria": "electronica", "peso_rango": (0.15, 0.25)},
            "impresora": {"precio_base": 150, "categoria": "electronica", "peso_rango": (5.0, 15.0)},
            "router_wifi": {"precio_base": 80, "categoria": "electronica", "peso_rango": (0.8, 2.0)},
            
            # Accesorios
            "mouse": {"precio_base": 25, "categoria": "accesorios", "peso_rango": (0.1, 0.3)},
            "teclado": {"precio_base": 60, "categoria": "accesorios", "peso_rango": (0.8, 1.5)},
            "auriculares": {"precio_base": 80, "categoria": "accesorios", "peso_rango": (0.2, 0.5)},
            "webcam": {"precio_base": 70, "categoria": "accesorios", "peso_rango": (0.1, 0.3)},
            "micrófono": {"precio_base": 90, "categoria": "accesorios", "peso_rango": (0.3, 1.0)},
            "altavoces": {"precio_base": 100, "categoria": "accesorios", "peso_rango": (1.0, 3.0)},
            "mousepad": {"precio_base": 20, "categoria": "accesorios", "peso_rango": (0.2, 0.8)},
            "soporte_monitor": {"precio_base": 45, "categoria": "accesorios", "peso_rango": (2.0, 5.0)},
            
            # Almacenamiento
            "disco_ssd": {"precio_base": 120, "categoria": "almacenamiento", "peso_rango": (0.1, 0.2)},
            "memoria_ram": {"precio_base": 80, "categoria": "almacenamiento", "peso_rango": (0.05, 0.1)},
            "disco_externo": {"precio_base": 90, "categoria": "almacenamiento", "peso_rango": (0.5, 1.0)},
            
            # Cables y conectividad
            "cable_hdmi": {"precio_base": 15, "categoria": "cables", "peso_rango": (0.1, 0.3)},
            "hub_usb": {"precio_base": 35, "categoria": "cables", "peso_rango": (0.2, 0.5)},
            "cargador_usb": {"precio_base": 18, "categoria": "cables", "peso_rango": (0.1, 0.4)},
            "cable_ethernet": {"precio_base": 12, "categoria": "cables", "peso_rango": (0.2, 0.5)},
            
            # Software
            "antivirus": {"precio_base": 50, "categoria": "software", "peso_rango": (0.0, 0.0)},
            "office_suite": {"precio_base": 120, "categoria": "software", "peso_rango": (0.0, 0.0)},
            "adobe_creative": {"precio_base": 300, "categoria": "software", "peso_rango": (0.0, 0.0)},
            
            # Gaming
            "gamepad": {"precio_base": 55, "categoria": "gaming", "peso_rango": (0.3, 0.8)},
            "headset_gaming": {"precio_base": 120, "categoria": "gaming", "peso_rango": (0.4, 0.9)},
            "silla_gaming": {"precio_base": 250, "categoria": "gaming", "peso_rango": (15.0, 25.0)}
        }
        
        productos = {}
        
        for nombre, config in productos_config.items():
            # Variación de precio ±40%
            variacion_precio = random.uniform(0.6, 1.4)
            precio_final = int(config["precio_base"] * variacion_precio)
            
            # Stock realista basado en popularidad del producto
            popularidad = random.randint(1, 100)
            stock_base = max(5, int(100 * (popularidad / 100) * random.uniform(0.5, 2.0)))
            
            # Peso aleatorio en el rango especificado
            peso_min, peso_max = config["peso_rango"]
            peso = round(random.uniform(peso_min, peso_max), 1) if peso_max > 0 else 0.0
            
            productos[nombre] = {
                "precio": precio_final,
                "stock": stock_base,
                "categoria": config["categoria"],
                "marca": random.choice(marcas),
                "rating": round(random.uniform(3.2, 4.9), 1),
                "descuento": random.choice([0, 5, 10, 15, 20, 25]),
                "tiempo_entrega": random.choice([1, 2, 3, 5, 7, 10]),
                "garantia_meses": random.choice([6, 12, 24, 36]),
                "peso_kg": peso,
                "popularidad": popularidad,
                "color": random.choice(["Negro", "Blanco", "Gris", "Azul", "Rojo"]),
                "disponible_online": random.choice([True, True, True, False]),  # 75% online
                "envio_gratis": precio_final > 50,  # Envío gratis si >50€
                "fecha_lanzamiento": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            }
        
        return productos
    
    def _generar_promociones(self) -> Dict:
        """Genera promociones activas."""
        promociones = {}
        num_promociones = random.randint(3, 8)
        productos_en_promo = random.sample(list(self.productos.keys()), k=num_promociones)
        
        tipos_promo = ["liquidacion", "oferta_flash", "descuento_volumen", "black_friday", "lanzamiento"]
        
        for producto in productos_en_promo:
            tipo_promo = random.choice(tipos_promo)
            
            if tipo_promo == "descuento_volumen":
                promociones[producto] = {
                    "descuento_extra": random.choice([5, 10, 15]),
                    "tipo": tipo_promo,
                    "minimo_cantidad": random.choice([5, 10, 20]),
                    "valido_hasta": "2025-08-31",
                    "descripcion": f"Descuento adicional por compra de {random.choice([5, 10, 20])}+ unidades"
                }
            else:
                promociones[producto] = {
                    "descuento_extra": random.choice([10, 15, 20, 25, 30]),
                    "tipo": tipo_promo,
                    "valido_hasta": "2025-07-31",
                    "descripcion": f"Promoción especial {tipo_promo.replace('_', ' ')}"
                }
        
        return promociones
    
    def buscar_producto_avanzado(self, nombre: str) -> str:
        """Búsqueda avanzada con información rica."""
        nombre_norm = nombre.lower().replace(" ", "_").replace("-", "_")
        
        # Búsqueda exacta
        if nombre_norm in self.productos:
            return self._formatear_info_producto(nombre_norm)
        
        # Búsqueda fuzzy
        matches = self._buscar_fuzzy(nombre_norm)
        
        if len(matches) == 1:
            return self._formatear_info_producto(matches[0])
        elif len(matches) > 1:
            return f"Productos similares encontrados: {', '.join(matches[:5])}"
        else:
            return f"Producto '{nombre}' no encontrado en nuestro catálogo"
    
    def _buscar_fuzzy(self, nombre: str) -> List[str]:
        """Búsqueda fuzzy inteligente."""
        matches = []
        palabras_busqueda = nombre.split("_")
        
        for producto in self.productos.keys():
            # Coincidencia exacta
            if nombre == producto:
                return [producto]
            
            # Coincidencia parcial
            if nombre in producto or producto in nombre:
                matches.append(producto)
                continue
            
            # Coincidencia por palabras
            palabras_producto = producto.split("_")
            coincidencias = sum(1 for palabra in palabras_busqueda if any(palabra in pp for pp in palabras_producto))
            
            if coincidencias > 0:
                matches.append(producto)
        
        # Ordenar por relevancia (más coincidencias primero)
        matches.sort(key=lambda x: (
            len([p for p in palabras_busqueda if p in x]),  # Coincidencias de palabras
            -len(x)  # Productos con nombres más cortos primero
        ), reverse=True)
        
        return matches
    
    def _formatear_info_producto(self, nombre: str) -> str:
        """Formatea la información de un producto."""
        p = self.productos[nombre]
        precio_original = p["precio"]
        descuento_total = p["descuento"]
        
        # Aplicar promoción si existe
        promocion_info = ""
        if nombre in self.promociones_activas:
            promo = self.promociones_activas[nombre]
            if promo["tipo"] == "descuento_volumen":
                promocion_info = f"\n🎯 {promo['descripcion']} - {promo['descuento_extra']}% extra"
            else:
                descuento_total += promo["descuento_extra"]
                promocion_info = f"\n🔥 {promo['descripcion']} - {promo['descuento_extra']}% extra!"
        
        precio_final = precio_original * (1 - descuento_total/100)
        
        info = f"""📦 {nombre.upper().replace('_', ' ')}
💰 Precio: €{precio_original} → €{precio_final:.2f} ({descuento_total}% desc.)
📊 Stock: {p['stock']} unidades
⭐ Rating: {p['rating']}/5.0
🏷️ Marca: {p['marca']}
📦 Categoría: {p['categoria']}
🚚 Entrega: {p['tiempo_entrega']} días
🔧 Garantía: {p['garantia_meses']} meses
⚖️ Peso: {p['peso_kg']} kg
🎨 Color: {p['color']}
🌐 Online: {'Sí' if p['disponible_online'] else 'Solo tienda'}
📮 Envío: {'Gratis' if p['envio_gratis'] else 'Con coste'}{promocion_info}"""
        
        return info
    
    def verificar_stock_complejo(self, nombre: str, cantidad: int) -> Dict:
        """Verificación de stock con lógica de negocio."""
        nombre_norm = nombre.lower().replace(" ", "_").replace("-", "_")
        
        if nombre_norm not in self.productos:
            sugerencias = self._buscar_fuzzy(nombre_norm)
            return {
                "success": False, 
                "message": "Producto no encontrado",
                "sugerencias": sugerencias[:3]
            }
        
        p = self.productos[nombre_norm]
        stock_actual = p["stock"]
        
        if stock_actual >= cantidad:
            # Verificar promoción de volumen
            promocion_volumen = self._verificar_promocion_volumen(nombre_norm, cantidad)
            
            return {
                "success": True,
                "stock_disponible": stock_actual,
                "cantidad_solicitada": cantidad,
                "stock_restante": stock_actual - cantidad,
                "tiempo_entrega": p["tiempo_entrega"],
                "promocion_volumen": promocion_volumen,
                "recomendacion": "✅ Stock suficiente - proceder con pedido"
            }
        else:
            deficit = cantidad - stock_actual
            tiempo_restock = random.randint(5, 30)
            alternativas = self._buscar_alternativas(nombre_norm)
            
            return {
                "success": False,
                "stock_disponible": stock_actual,
                "cantidad_solicitada": cantidad,
                "deficit": deficit,
                "tiempo_restock_dias": tiempo_restock,
                "alternativas": alternativas,
                "pedido_parcial_posible": stock_actual > 0,
                "recomendacion": f"⚠️ Stock insuficiente. Disponible: {stock_actual} unidades"
            }
    
    def _verificar_promocion_volumen(self, nombre: str, cantidad: int) -> Dict:
        """Verifica si aplica promoción por volumen."""
        if nombre in self.promociones_activas:
            promo = self.promociones_activas[nombre]
            if promo["tipo"] == "descuento_volumen" and cantidad >= promo["minimo_cantidad"]:
                return {
                    "aplica": True,
                    "descuento_extra": promo["descuento_extra"],
                    "descripcion": promo["descripcion"]
                }
        
        return {"aplica": False}
    
    def _buscar_alternativas(self, nombre: str) -> List[str]:
        """Busca productos alternativos de la misma categoría."""
        if nombre not in self.productos:
            return []
        
        categoria_objetivo = self.productos[nombre]["categoria"]
        precio_original = self.productos[nombre]["precio"]
        
        alternativas = []
        for prod, info in self.productos.items():
            if (info["categoria"] == categoria_objetivo and 
                prod != nombre and 
                info["stock"] > 0 and
                abs(info["precio"] - precio_original) < precio_original * 0.5):  # Precio similar ±50%
                alternativas.append(prod)
        
        # Ordenar por rating y disponibilidad
        alternativas.sort(
            key=lambda x: (
                self.productos[x]["rating"], 
                self.productos[x]["stock"],
                -abs(self.productos[x]["precio"] - precio_original)
            ), 
            reverse=True
        )
        
        return alternativas[:3]
    
    def exportar_inventario_json(self, archivo="inventario_completo.json"):
        """Exporta el inventario completo a JSON para consulta."""
        datos_completos = {
            "productos": self.productos,
            "promociones": self.promociones_activas,
            "estadisticas": {
                "total_productos": len(self.productos),
                "total_promociones": len(self.promociones_activas),
                "categorias": list(set(p["categoria"] for p in self.productos.values())),
                "marcas": list(set(p["marca"] for p in self.productos.values())),
                "rango_precios": {
                    "min": min(p["precio"] for p in self.productos.values()),
                    "max": max(p["precio"] for p in self.productos.values())
                }
            }
        }
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_completos, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Inventario exportado a {archivo}")
    
    def mostrar_resumen(self):
        """Muestra un resumen del inventario."""
        print(f"\n🏪 RESUMEN DEL INVENTARIO")
        print(f"{'='*40}")
        print(f"📦 Total productos: {len(self.productos)}")
        print(f"🎯 Promociones activas: {len(self.promociones_activas)}")
        
        # Por categoría
        categorias = {}
        for producto, info in self.productos.items():
            cat = info["categoria"]
            categorias[cat] = categorias.get(cat, 0) + 1
        
        print(f"\n📊 Por categoría:")
        for cat, count in sorted(categorias.items()):
            print(f"  • {cat}: {count} productos")
        
        # Stock total
        stock_total = sum(p["stock"] for p in self.productos.values())
        print(f"\n📦 Stock total: {stock_total:,} unidades")
        
        # Precios
        precios = [p["precio"] for p in self.productos.values()]
        print(f"💰 Rango precios: €{min(precios)} - €{max(precios)}")

# =============================================================================
# FUNCIONES UTILITARIAS
# =============================================================================

def crear_inventario_fresco():
    """Crea un inventario completamente nuevo."""
    inventario = InventarioComplejo()
    inventario.regenerar_inventario()
    inventario.mostrar_resumen()
    inventario.exportar_inventario_json()
    return inventario

def cargar_inventario_existente():
    """Carga inventario existente o crea uno nuevo."""
    inventario = InventarioComplejo()
    inventario.mostrar_resumen()
    return inventario

if __name__ == "__main__":
    print("🛒 Generador de Inventario para Experimentos de Agentes")
    print("="*60)
    
    # Crear o cargar inventario
    opcion = input("¿Crear nuevo inventario? (s/n): ").lower().strip()
    
    if opcion == 's':
        inventario = crear_inventario_fresco()
    else:
        inventario = cargar_inventario_existente()
    
    # Exportar para uso en otros scripts
    inventario.exportar_inventario_json()
    
    print(f"\n✅ Inventario listo para usar en experimentos!")
    print(f"📁 Archivos generados:")
    print(f"  • inventario_cache.pkl (cache binario)")
    print(f"  • inventario_completo.json (para consulta)")