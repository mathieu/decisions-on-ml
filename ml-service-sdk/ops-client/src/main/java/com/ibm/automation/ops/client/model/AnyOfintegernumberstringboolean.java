/*
 * IBM Confidential
 * OCO Source Materials
 * 5737-I23
 * Copyright IBM Corp. 2019, 2020
 * The source code for this program is not published or otherwise divested of its trade secrets, irrespective of what has been deposited with the U.S Copyright Office.
 */

package com.ibm.automation.ops.client.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.JsonAdapter;
import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Map;

@JsonAdapter(AnySerializer.class)
public class AnyOfintegernumberstringboolean {

    @Expose(serialize = false, deserialize = false)
    final AnyType type;

    @Expose(serialize = false, deserialize = false)
    Object value;

    public AnyOfintegernumberstringboolean(int i) {
        type = AnyType.INTEGER;
        value = new Integer(i);
    }

    public AnyOfintegernumberstringboolean(long l) {
        type = AnyType.INTEGER;
        value = new Long(l);
    }


    public AnyOfintegernumberstringboolean(double d) {
        type = AnyType.NUMBER;
        value = new BigDecimal(d);
    }

    public AnyOfintegernumberstringboolean(BigDecimal b) {
        type = AnyType.NUMBER;
        value = b;
    }

    public AnyOfintegernumberstringboolean(BigInteger b) {
        type = AnyType.NUMBER;
        value = b;
    }

    public AnyOfintegernumberstringboolean(boolean b) {
        type = AnyType.BOOLEAN;
        value = new Boolean(b);
    }

    public AnyOfintegernumberstringboolean(String s) {
        type = AnyType.STRING;
        value = s;
    }

    public AnyOfintegernumberstringboolean(char c) {
        type = AnyType.STRING;
        value = "" + c;
    }

    public static AnyOfintegernumberstringboolean build(Object obj) {

        if (obj instanceof Integer) {
            return new AnyOfintegernumberstringboolean((Integer) obj);
        } else if (obj instanceof Short) {
            return new AnyOfintegernumberstringboolean((Short) obj);
        } else if (obj instanceof Byte) {
            return new AnyOfintegernumberstringboolean((Byte) obj);
        } else if (obj instanceof BigDecimal) {
            return new AnyOfintegernumberstringboolean((BigDecimal) obj);
        } else if (obj instanceof BigInteger) {
            return new AnyOfintegernumberstringboolean((BigInteger) obj);
        } else if (obj instanceof Double) {
            return new AnyOfintegernumberstringboolean((Double) obj);
        } else if (obj instanceof Float) {
            return new AnyOfintegernumberstringboolean((Float) obj);
        } else if (obj instanceof Long) {
            return new AnyOfintegernumberstringboolean((Long) obj);
        } else if (obj instanceof Boolean) {
            return new AnyOfintegernumberstringboolean((Boolean) obj);
        } else if (obj instanceof String) {
            return new AnyOfintegernumberstringboolean((String) obj);
        } else if (obj instanceof Character) {
            return new AnyOfintegernumberstringboolean((Character) obj);
        } else {
            return null;
            // TODO or return obj.toString(); ?? to be more tolerant
        }
    }

    public static AnyOfintegernumberstringboolean create(Map<String, Object> map) {
        return build(map.get("value"));
    }

    public Object getValue() {
        return value;
    }

    @Override
    public String toString() {
//        if (type == AnyType.STRING) {
//            return "\"" + value.toString() + "\"";
//        }

        return value.toString();
    }

    public String toJsonType() {
        switch (type) {
            case INTEGER:
                return "integer";
            case NUMBER:
                return "number";
            case STRING:
                return "string";
            case BOOLEAN:
                return "bool";
            default:
                return null;
            // TODO return "string" ?? to be more tolerant
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof AnyOfintegernumberstringboolean))
            return false;
        if (obj == this)
            return true;

        AnyOfintegernumberstringboolean rhs = (AnyOfintegernumberstringboolean) obj;
        return new EqualsBuilder().
                // if deriving: appendSuper(super.equals(obj)).
                        append(type, rhs.type).
                        append(value, rhs.value).
                        isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 31). // two randomly chosen prime numbers
                // if deriving: appendSuper(super.hashCode()).
                        append(type).
                        append(value).
                        toHashCode();
    }

    enum AnyType {
        INTEGER,
        NUMBER,
        BOOLEAN,
        STRING
    }
}
